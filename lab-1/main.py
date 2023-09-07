from typing import Tuple, List

import pandas as pd

from util.LogDTO import LogDTO
from util.loader import load_logs_from_file
from util.mapper import map_logs_to_dataframe
from task.hypothesis import check_if_items_added_more_from_catalogue_than_after_search

if __name__ == '__main__':
    data: Tuple[List[LogDTO], int] = load_logs_from_file("../data/access.log")
    df: pd.DataFrame = map_logs_to_dataframe(data[0], 50)
    print(df.to_string())
    print(check_if_items_added_more_from_catalogue_than_after_search(df))
