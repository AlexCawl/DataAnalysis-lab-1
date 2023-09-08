from typing import Tuple

import pandas as pd

from lab_1.util.decorators import measure_execution_time


# Гипотеза №6
# Общее число запросов КАТАЛОГ, меньше чем ПОИСК

@measure_execution_time
def check_count_of_catalogue_and_search(dataframe: pd.DataFrame) -> Tuple[str, str]:
    h0: str = "h0: Общее число запросов КАТАЛОГ, меньше чем ПОИСК"
    h1: str = "h1: Общее число запросов ПОИСК, меньше чем КАТАЛОГ"

    catalog_counts: int = len(dataframe[dataframe["URL"] == "/catalog.phtml"])
    search_counts: int = len(dataframe[dataframe["URL"] == "/search.phtml"])

    return h0 if catalog_counts < search_counts else h1, f"catalog - {catalog_counts} | search - {search_counts}"
