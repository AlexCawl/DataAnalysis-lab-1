import re
from typing import Dict

from .constants import *


# Example:
# 79.239.214.126 - - [1/Jun/2015:00:00:07 +04:00] "POST /catalog.phtml HTTP 1.1" 200 2005 ID5075

# Regex:
# r'\d+\.\d+\.\d+\.\d+|(?<=\")(.*)(?=\")|(?<=\[)(.*)(?=\])|\d+|ID\d+

def parse_into_tokens(line: str) -> Dict[str, str]:
    request: str = re.findall(r'(?<=\")(.*)(?=\")', line)[0]
    return {
        IP_ADDRESS: re.findall(r'\d+\.\d+\.\d+\.\d+', line)[0],
        URL: request.split(' ')[1],
        DATETIME: re.findall(r'(?<=\[)(.*)(?=\])', line)[0],
        HTTP_CODE: re.findall(r'(\d+)', line)[-3],
        ID: re.findall(r'ID\d+', line)[0],
        HTTP_METHOD: request.split(' ')[0]
    }
