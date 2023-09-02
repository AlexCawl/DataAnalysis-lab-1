from typing import List, TextIO


def load_data(path: str) -> List[str]:
    file: TextIO = open(file=path, mode="r")
    content: List[str] = file.readlines()
    # TODO to LIST[DTO]
    return content
