from typing import Tuple, List

import pandas as pd

from lab_1.test import debug
from task.hypothesis_1 import check_items_added_from_catalogue_rather_search
from task.hypothesis_2 import check_if_added_few_items_more_often_from_catalog_then_from_search
from task.hypothesis_3 import check_if_item_added_from_search_it_is_single
from task.hypothesis_4 import check_item_chosen_clusters
from util.LogDTO import LogDTO
from util.decorators import measure_execution_time
from util.loader import load_logs_from_file
from util.mapper import map_logs_to_dataframe


@measure_execution_time
def check_hypothesises(dataframe: pd.DataFrame):
    r1: Tuple[str, str] = check_items_added_from_catalogue_rather_search(dataframe)
    print(f"#1\n{r1[0]}\n{r1[1]}\n")
    r2: Tuple[str, str] = check_if_added_few_items_more_often_from_catalog_then_from_search(dataframe)
    print(f"#2\n{r2[0]}\n{r2[1]}\n")
    r3: Tuple[str, str] = check_if_item_added_from_search_it_is_single(dataframe)
    print(f"#3\n{r3[0]}\n{r3[1]}\n")
    r4 = check_item_chosen_clusters(dataframe)
    print(f"#4\n{r4[0]}\n{r4[1]}\n")


if __name__ == '__main__':
    data: Tuple[List[LogDTO], int] = load_logs_from_file("../data/access.log")
    df: pd.DataFrame = map_logs_to_dataframe(data[0], 100000)
    debug(df)
    check_hypothesises(df)
