from typing import Tuple, List

import pandas as pd

from task.hypothesis_1 import check_items_added_from_catalogue_rather_search
from util.LogDTO import LogDTO
from util.loader import load_logs_from_file
from util.mapper import map_logs_to_dataframe

if __name__ == '__main__':
    data: Tuple[List[LogDTO], int] = load_logs_from_file("../data/access.log")
    df: pd.DataFrame = map_logs_to_dataframe(data[0], 10000)
    result: Tuple[str, str] = check_items_added_from_catalogue_rather_search(df)
    print(result)
