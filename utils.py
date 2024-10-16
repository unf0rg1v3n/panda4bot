import re
from datetime import datetime


def parse_date_from_message(message: str):

    match_time = re.search("([01][0-9]|2[0-3]):[0-5][0-9]", message)
    match_date = re.search("(0[1-9]|[12][0-9]|3[01])[./](0[1-9]|1[0-2])[./](20[3-9][0-9]|202[4-9])", message)

    if match_time is None:
        return 0

    if match_date is None:
        result = datetime.strptime(f"{datetime.now().date().strftime("%d.%m.%Y")} {match_time.group()}", "%d.%m.%Y %H:%M")
        return (result - datetime.now()).total_seconds()

    result = f"{match_date.group()} {match_time.group()}"
    date_in_seconds = (datetime.strptime(result, "d.%m.%Y %H:%M") - datetime.now()).total_seconds()
    return date_in_seconds


def parse_text_from_message(message: str):
    match = re.search("", message)
    return match.group()
