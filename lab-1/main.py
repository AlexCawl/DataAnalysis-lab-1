from typing import Tuple, List

import pandas as pd

from util.LogDTO import LogDTO
from util.loader import load_logs_from_file
from util.mapper import map_logs_to_dataframe
from task.hypothesis_1 import check_something

if __name__ == '__main__':
    data: Tuple[List[LogDTO], int] = load_logs_from_file("../data/access.log")
    df: pd.DataFrame = map_logs_to_dataframe(data[0])
    print(df)
    print(check_something(df))
