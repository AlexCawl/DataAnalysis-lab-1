from typing import Tuple, List

import pandas as pd

from LogDTO import LogDTO
from mapper import map_logs_to_dataframe
from reader import load_logs_from_file

if __name__ == '__main__':
    data: Tuple[List[LogDTO], int] = load_logs_from_file("../data/access.log")
    df: pd.DataFrame = map_logs_to_dataframe(data[0])
    print(df)
