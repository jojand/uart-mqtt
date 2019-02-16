import re

MQTT_LINE_REGEX = r'\[MQTT\] ([a-z0-9/_]+) ([-a-z0-9/_.]+)\*'
TOPIC_MATCH_INDEX = 1
PAYLOAD_MATCH_INDEX = 2


def parse_uart_line(input_string):

    match = re.match(MQTT_LINE_REGEX, input_string)

    topic_match = match.group(TOPIC_MATCH_INDEX) if match and match.group(TOPIC_MATCH_INDEX) else ''
    payload_match = match.group(PAYLOAD_MATCH_INDEX) if match and match.group(PAYLOAD_MATCH_INDEX) else ''

    if match:
        result = (match.group(TOPIC_MATCH_INDEX) is not None) and (match.group(PAYLOAD_MATCH_INDEX) is not None)
    else:
        result = False

    return result, topic_match, payload_match
