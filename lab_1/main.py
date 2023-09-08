from typing import Tuple, List

import pandas as pd

from lab_1.test import debug
from task.hypothesis_1 import check_items_added_from_catalogue_rather_search
from task.hypothesis_2 import check_if_added_few_items_more_often_from_catalog_then_from_search
from util.LogDTO import LogDTO
from util.decorators import measure_execution_time
from util.loader import load_logs_from_file
from util.mapper import map_logs_to_dataframe


@measure_execution_time
def check_hypothesises(dataframe: pd.DataFrame):
    h1: str = """
        Гипотеза №1
        При использовании КАТАЛОГА пользователь добавляет предмет в корзину чаще, чем после ПОИСКА.
    """
    r1: Tuple[str, str] = check_items_added_from_catalogue_rather_search(dataframe)
    print(f"{h1}\n{r1[0]}\n{r1[1]}\n\n")
    h2: str = """
        Гипотеза №2
        При добавлении предмета с использованием КАТАЛОГА пользователь добавляет следующий предмет в корзину чаще, чем при использовании ПОИСКА
    """
    r2: Tuple[str, str] = check_if_added_few_items_more_often_from_catalog_then_from_search(dataframe)
    print(f"{h2}\n{r2[0]}\n{r2[1]}\n\n")
    # TODO other hypothesis checking add


if __name__ == '__main__':
    data: Tuple[List[LogDTO], int] = load_logs_from_file("../data/access.log")
    df: pd.DataFrame = map_logs_to_dataframe(data[0], 10000)
    debug(df)
    check_hypothesises(df)
