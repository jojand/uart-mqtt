import re

MQTT_LINE_REGEX = r'\[MQTT\] ([a-z0-9/_]+) ([-a-z0-9/_.]+)\*'
TOPIC_MATCH_INDEX = 1
PAYLOAD_MATCH_INDEX = 2


def parse_uart_line(input_string):

    match = re.match(MQTT_LINE_REGEX, input_string)

    topic_match = match[TOPIC_MATCH_INDEX] if match and match[TOPIC_MATCH_INDEX] else ''
    payload_match = match[PAYLOAD_MATCH_INDEX] if match and match[PAYLOAD_MATCH_INDEX] else ''

    if match:
        result = (match[TOPIC_MATCH_INDEX] is not None) and (match[PAYLOAD_MATCH_INDEX] is not None)
    else:
        result = False

    return result, topic_match, payload_match
