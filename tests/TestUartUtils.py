import unittest
from uart_utils.parser import parse_uart_line


class TestUartUtils(unittest.TestCase):

    def test_parse_uart_line_1(self):
        result, topic, payload = parse_uart_line('[MQTT] test/topic test_payload*\n\r')
        assert result
        assert topic == 'test/topic'
        assert payload == 'test_payload'

    def test_parse_uart_line_2(self):
        result, topic, payload = parse_uart_line('[MQTT] test/topic test_payload*\n')
        assert result
        assert topic == 'test/topic'
        assert payload == 'test_payload'

    def test_parse_uart_line_3(self):
        result, topic, payload = parse_uart_line('[MQTT] test/topic test_payload*')
        assert result
        assert topic == 'test/topic'
        assert payload == 'test_payload'

    def test_parse_uart_line_4(self):
        result, topic, payload = parse_uart_line('[MQTT] test/topic_1 123456*')
        assert result
        assert topic == 'test/topic_1'
        assert payload == '123456'

    def test_parse_uart_line_5(self):
        result, topic, payload = parse_uart_line('[MQTT] test/topic 0.0*')
        assert result
        assert topic == 'test/topic'
        assert payload == '0.0'

    def test_parse_uart_line_6(self):
        result, topic, payload = parse_uart_line('[MQTT] test/topic -1.0*')
        assert result
        assert topic == 'test/topic'
        assert payload == '-1.0'

    def test_parse_uart_line_7(self):
        result, topic, payload = parse_uart_line('[MQ TT] test/topic 0.0*')
        assert not result
        assert topic == ''
        assert payload == ''

    def test_parse_uart_line_8(self):
        result, topic, payload = parse_uart_line('MQTT] test/topic 0.0*')
        assert not result
        assert topic == ''
        assert payload == ''

    def test_parse_uart_line_9(self):
        result, topic, payload = parse_uart_line('[MQTT] test/topic 0.0')
        assert not result
        assert topic == ''
        assert payload == ''


if __name__ == '__main__':
    unittest.main()
