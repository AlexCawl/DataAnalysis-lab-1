from typing import Tuple, Callable

import pandas as pd

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time
from lab_1.util.extensions import is_catalogue_request, is_search_request


# №19 Вопрос: Какова удовлетворенность клиентов от взаимодействия с сайтом?
# Гипотеза: при формировании своей продуктовой корзины, покупатель с большей степенью воспользуется КАТАЛОГОМ, нежели ПОИСКОМ

@measure_execution_time
def main_19(dataframe: pd.DataFrame) -> str:
    h0: str = "При формировании своей продуктовой корзины, покупатель с большей степенью воспользуется КАТАЛОГОМ, нежели ПОИСКОМ"
    h1: str = "При формировании своей продуктовой корзины, покупатель с большей степенью воспользуется ПОИСКОМ, нежели КАТАЛОГОМ"
    condition: Callable[[int], bool] = lambda c, s: c > s

    def user_last_request(_dataframe: pd.DataFrame, log_index: int, user: str) -> int:
        for i in range(log_index, -1, -1):
            log: pd.Series = _dataframe.loc[i]
            if str(log[USER]) == user:
                endpoint: str = str(log[ENDPOINT])
                if is_catalogue_request(endpoint):
                    return 0
                elif is_search_request(endpoint):
                    return 1
        return -1

    catalog_count: int = 0
    search_count: int = 0

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[USER])
        url: str = str(row[ENDPOINT])

        if url.startswith(ADD_BASKET):
            last_request: int = user_last_request(dataframe, index, user_id)
            if last_request == 0:
                catalog_count += 1
            elif last_request == 1:
                search_count += 1

    return h0 if condition(catalog_count, search_count) else h1
