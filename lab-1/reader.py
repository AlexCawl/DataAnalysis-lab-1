from typing import TextIO
from LogDTO import LogDTO
from parser import parse


def load_logs_from_file(path: str) -> tuple[list[LogDTO], int]:
    file: TextIO = open(file=path, mode="r")
    content: list[str] = file.readlines()
    logs: list[LogDTO] = []
    fail_count: int = 0

    for line in content:
        try:
            log: LogDTO = parse(line)
            logs.append(log)
        except Exception:
            fail_count += 1
    return logs, fail_count
