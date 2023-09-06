# created by GlaDGoD
# log example 79.239.214.126 - - [1/Jun/2015:00:00:07 +04:00] "POST /catalog.phtml HTTP 1.1" 200 2005 ID5075
# regex: r'\d+\.\d+\.\d+\.\d+|(?<=\")(.*)(?=\")|(?<=\[)(.*)(?=\])|\d+|ID\d+
import re
from typing import List


def parser(log: str) -> dict[str, str]:
    return {
        "ip": re.findall(r'\d+\.\d+\.\d+\.\d+', log)[0],
        "request": re.findall(r'(?<=\")(.*)(?=\")', log)[0],
        "date": re.findall(r'(?<=\[)(.*)(?=\])', log)[0],
        "code": re.findall(r'\d+', log)[0],
        "response": re.findall(r'\d+', log)[1],
        "id": re.findall(r'ID\d+', log)[0],
    }
