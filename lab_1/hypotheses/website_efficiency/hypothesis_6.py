from typing import Tuple, Callable, Any

import pandas as pd

from lab_1.util.decorators import measure_execution_time
from lab_1.util.constants import *


# №6
# Вопрос: Какие есть возможности по повышению эффективности интернет-магазина?
# Гипотеза: Общее число запросов КАТАЛОГ, меньше чем ПОИСК

@measure_execution_time
def compute_6(dataframe: pd.DataFrame) -> Tuple[str, str]:
    h0: str = "Общее число запросов КАТАЛОГ меньше чем ПОИСК"
    h1: str = "Общее число запросов КАТАЛОГ не меньше чем ПОИСК"
    condition: Callable[[int, int], bool] = lambda c, s: c < s

    catalogue_count = len(dataframe[dataframe[URL] == "/catalog.phtml"])
    search_count = len(dataframe[dataframe[URL] == "/search.phtml"])

    return (
        h0 if condition(catalogue_count, search_count) else h1,
        f"catalogue_count={catalogue_count}; search_count={search_count}"
    )
