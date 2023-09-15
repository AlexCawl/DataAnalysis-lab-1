from typing import Tuple, Dict, Callable

import pandas as pd

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time


# №16
# Вопрос: Какова удовлетворенность клиентов от взаимодействия с сайтом?
# Гипотеза: Среднее количество элементов в корзине клиента больше, чем $VAL

@measure_execution_time
def compute(dataframe: pd.DataFrame, comparable_value: float) -> Tuple[str, str]:
    h0: str = "Среднее количество элементов в корзине клиента больше чем {VAL:.2f}"
    h1: str = "Среднее количество элементов в корзине клиента не больше чем {VAL:.2f}"
    condition: Callable[[int], bool] = lambda e: e > comparable_value
    users: Dict[str, bool] = dict()
    add_item_count: int = 0
    users_count: int = 0

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[ID])
        url: str = str(row[URL])

        if url.startswith(ADDBASKET):
            add_item_count += 1
            if users.get(user_id) is None:
                users.update({user_id: True})
                users_count += 1

    result: float = add_item_count / users_count
    return (
        h0.format(VAL=result) if condition(result) else h1.format(VAL=result),
        f"add_item_count={add_item_count}; users_count={users_count}; result={add_item_count / users_count}"
    )
