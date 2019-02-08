import argparse
import serial
import paho.mqtt.client as mqtt
from uart_utils.parser import parse_uart_line

SERIAL_TIMEOUT = 5
KEEPALIVE = 60
mqtt_cli = None


def process_args():
    parser = argparse.ArgumentParser(description='Uart MQTT gateway')
    parser.add_argument('--port', help='Serial port to connect to', required=True)
    parser.add_argument('--baud', help='Serial port baudrate', required=True)
    parser.add_argument('--mqtt_host', help='MQTT host', required=True)
    parser.add_argument('--mqtt_port', help='MQTT port', required=True)
    args = parser.parse_args()
    return args


def connect_to_serial(port, baud):
    print('Connecting to serial {} ad baud {}'.format(port, baud))
    ser = serial.Serial(port, baud, timeout=SERIAL_TIMEOUT)
    print('connected')
    return ser


def process_serial(line):
    global mqtt_cli
    result, topic, payload = parse_uart_line(line.decode())
    if not result:
        print('Parse error!')
    else:
        mqtt_cli.publish(topic, payload)
    pass


def main():
    args = process_args()
    print('UART MQTT gateway start ...')
    print('Connecting to MQTT at host {}, port {}'.format(args.mqtt_host, args.mqtt_port))

    global mqtt_cli
    mqtt_cli = mqtt.Client()
    mqtt_cli.connect(host=args.mqtt_host,
                     port=int(args.mqtt_port),
                     keepalive=KEEPALIVE)

    print('connected')

    with connect_to_serial(args.port, args.baud) as ser:
        while True:
            line = ser.readline()
            if line:
                process_serial(line)


if __name__ == '__main__':
    main()
