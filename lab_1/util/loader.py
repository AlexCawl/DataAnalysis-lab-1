from typing import TextIO, Tuple, List

from .LogDTO import LogDTO
from .decorators import measure_execution_time
from .processor import parse


@measure_execution_time
def load_logs_from_file(path: str) -> Tuple[List[LogDTO], int]:
    file: TextIO = open(file=path, mode="r")
    content: List[str] = file.readlines()
    logs: List[LogDTO] = []
    fail_count: int = 0

    for line in content:
        try:
            log: LogDTO = parse(line)
            logs.append(log)
        except Exception:
            fail_count += 1
    print(f"Loading data processed with {fail_count} fails")
    return logs, fail_count
