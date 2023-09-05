from typing import List, TextIO
from logparser import parser
from loginfo import LogInfo
def load_data(path: str) -> List[str]:
    file: TextIO = open(file=path, mode="r")
    content: List[str] = file.readlines()
    # TODO to LIST[DTO]
    return content

loginfoDatabase = []
for log in load_data("../access.log"):
    try:
        parse = parser(log)
    except:
        continue
    loginfoDatabase.append(LogInfo(
        parse["ip"],
        parse["date"],
        parse["request"],
        parse["code"],
        parse["response"],
        parse["id"]
    ))
