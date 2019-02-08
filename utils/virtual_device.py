import argparse
import serial
from time import sleep

SERIAL_TIMEOUT = 1


def process_args():
    parser = argparse.ArgumentParser(description='Test device')
    parser.add_argument('--port', help='Serial port to connect to', required=True)
    parser.add_argument('--baud', help='Serial port baudrate', required=True)
    args = parser.parse_args()
    return args


def connect_to_serial(port, baud):
    print('Connecting to serial ...')
    ser = serial.Serial(port, baud, timeout=SERIAL_TIMEOUT)
    print('connected')
    return ser


if __name__ == '__main__':
    print('UART virtual device start ...')
    args = process_args()

    with connect_to_serial(args.port, args.baud) as ser:
        i = 0
        while True:
            message = '[MQTT] test/topic {}.0*\n'.format(i).encode()
            print('sending message {}'.format(message))
            ser.write(message)
            i = i + 1
            sleep(1)
