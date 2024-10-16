import re
from datetime import datetime


def parse_date_from_message(message: str):

    match_time = re.search("([01][0-9]|2[0-3]):[0-5][0-9]", message)
    #match_date = re.search("(0[1-9]|[12][0-9]|3[01])[./](0[1-9]|1[0-2])[./](20[3-9][0-9]|202[4-9])", message)

    # if match_date is None:
    #     return datetime.strptime(f"{datetime.now().date().strftime("%d.%m.%Y")} {match_time.group()}", "%Y.%m.%d %H:%M")

    # result = f"{match_date.group()} {match_time.group()}"
    return datetime.strptime(match_time.group(), "%H:%M").time()


def parse_text_from_message(message: str):
    match = re.search("", message)
    return match.group()


#print(datetime.now().date().strftime("%d.%m.%Y"))
print(parse_date_from_message("/set 12:44"))
# print(parse_text_from_message("/set 13:30 thisi is some messagE  AA Da"))
