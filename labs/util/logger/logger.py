import datetime
from typing import Optional, TextIO, Dict


def access_log(path: Optional[str], log_file: str = "lab3.log") -> Optional[str]:
    if path is not None:
        return f"{path}/{log_file}"
    else:
        return None


def init_log(log_path: Optional[str] = None):
    if log_path is not None:
        file: TextIO = open(log_path, "w")
        file.write(f"TIME: {datetime.datetime.now()}" + "\n\n")
        file.close()
    else:
        print(f"TIME: {datetime.datetime.now()}")


def write_json_to_log(
        log: Dict[str, str],
        *, log_path: Optional[str] = None
) -> None:
    if log_path is not None:
        file: TextIO = open(log_path, "a")
        for key, value in log.items():
            file.write(f"{key}: {value}" + "\n")
        file.close()
    else:
        for key, value in log.items():
            print(f"{key}: {value}")


def write_raw_to_log(
        log: str,
        *, log_path: Optional[str] = None
) -> None:
    if log_path is not None:
        file: TextIO = open(log_path, "a")
        file.write(f"{log}" + "\n")
        file.close()
    else:
        print(f"{log}")
