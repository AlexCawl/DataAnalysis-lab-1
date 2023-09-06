import re

from constants import *
from LogDTO import LogDTO


# Example:
# 79.239.214.126 - - [1/Jun/2015:00:00:07 +04:00] "POST /catalog.phtml HTTP 1.1" 200 2005 ID5075

# Regex:
# r'\d+\.\d+\.\d+\.\d+|(?<=\")(.*)(?=\")|(?<=\[)(.*)(?=\])|\d+|ID\d+

def parse_into_tokens(log_as_line: str) -> dict[str, str]:
    request: str = re.findall(r'(?<=\")(.*)(?=\")', log_as_line)[0]
    return {
        IP_ADDRESS: re.findall(r'\d+\.\d+\.\d+\.\d+', log_as_line)[0],
        URL: request.split(" ")[1],
        DATETIME: re.findall(r'(?<=\[)(.*)(?=\])', log_as_line)[0],
        HTTP_CODE: re.findall(r'(\d+)', log_as_line)[-3],
        ID: re.findall(r'ID\d+', log_as_line)[0],
        HTTP_TYPE: request.split(" ")[0]
    }


def parse_into_dto(data: dict[str, str]) -> LogDTO:
    return LogDTO(
        data[IP_ADDRESS],
        data[DATETIME],
        data[HTTP_TYPE],
        data[URL],
        data[HTTP_CODE],
        data[ID]
    )


def parse(line: str) -> LogDTO:
    data: dict[str, str] = parse_into_tokens(line)
    return parse_into_dto(data)
