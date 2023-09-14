from typing import Tuple, Dict

import pandas as pd

from lab_1.util.Hypothesis import Hypothesis
from lab_1.util.decorators import measure_execution_time
from lab_1.util.constants import *

# №16
# Вопрос: Какова удовлетворенность клиентов от взаимодействия с сайтом?
# Гипотеза: Среднее количество элементов в корзине клиента больше, чем $VAL

@measure_execution_time
def compute(dataframe: pd.DataFrame, comparable_value: float) -> Tuple[str, str]:
    hypothesis: Hypothesis = Hypothesis(
        h0="Среднее количество элементов в корзине клиента больше, чем $VAL",
        h1="Среднее количество элементов в корзине клиента не больше, чем $VAL",
        condition=lambda x: x > comparable_value
    )

    users: Dict[str, bool] = dict()
    addbasket_count: int = 0
    users_count = 0

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[ID])
        url: str = str(row[URL])

        if url.startswith(ADDBASKET):
            addbasket_count += 1
            if users.get(user_id) is None:
                users.update({user_id: True})
                users_count += 1

    value: float = addbasket_count/users_count  # computed from dataframe
    return hypothesis.compute(value), f"{value}"