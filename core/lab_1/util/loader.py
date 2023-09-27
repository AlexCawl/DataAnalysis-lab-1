from typing import TextIO, List, Dict

from core.util.benchmarking.measuring import measure_execution_time
from .processor import parse_into_tokens


@measure_execution_time
def load_logs_from_file(path: str) -> List[Dict[str, str]]:
    file: TextIO = open(file=path, mode="r")
    content: List[str] = file.readlines()
    logs: List[Dict[str, str]] = []
    fail_count: int = 0

    for line in content:
        try:
            logs.append(parse_into_tokens(line))
        except Exception:
            fail_count += 1
    print(f"Loading data processed with {fail_count} fails")
    return logs
