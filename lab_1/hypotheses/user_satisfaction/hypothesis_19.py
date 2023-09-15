from typing import Tuple

import pandas as pd

from lab_1.util.Hypothesis import Hypothesis
from lab_1.util.decorators import measure_execution_time
from lab_1.util.constants import *

# №19
# Вопрос: Какова удовлетворенность клиентов от взаимодействия с сайтом?
# Гипотеза: при формировании своей продуктовой корзины, покупатель с большей степенью воспользуется КАТАЛОГОМ, нежели ПОИСКОМ

@measure_execution_time
def compute(dataframe: pd.DataFrame, comparable_value: float) -> Tuple[str, str]:
    hypothesis: Hypothesis = Hypothesis(
        h0="при формировании своей продуктовой корзины, покупатель с большей степенью воспользуется КАТАЛОГОМ, нежели ПОИСКОМ",
        h1="при формировании своей продуктовой корзины, покупатель с большей степенью воспользуется ПОИСКОМ, нежели КАТАЛОГОМ",
        condition=lambda x: x > comparable_value
    )

    def user_last_request(_dataframe: pd.DataFrame, _index: int, _user_id: str) -> int:
        for i in range(_index, -1, -1):
            _row: pd.Series = _dataframe.loc[i]
            if str(_row[ID]) == _user_id:
                _url: str = str(_row[URL])
                if _url.startswith(CATALOG):
                    return 0
                elif _url.startswith(SEARCH):
                    return 1
        return -1

    catalog_count: int = 0
    search_count: int = 0

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[ID])
        url: str = str(row[URL])

        if url.startswith(ADDBASKET):
            last_request: int = user_last_request(dataframe, index, user_id)
            if last_request == 0:
                catalog_count += 1
            elif last_request == 1:
                search_count += 1

    hypothesis: Hypothesis = Hypothesis(
        h0="при формировании своей продуктовой корзины, покупатель с большей степенью воспользуется КАТАЛОГОМ, нежели ПОИСКОМ",
        h1="при формировании своей продуктовой корзины, покупатель с большей степенью воспользуется ПОИСКОМ, нежели КАТАЛОГОМ",
        condition=lambda x: x > search_count
    )

    return hypothesis.compute(catalog_count), f"{catalog_count} | {search_count}"
