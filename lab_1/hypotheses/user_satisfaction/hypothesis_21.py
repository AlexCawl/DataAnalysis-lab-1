from typing import Tuple, Dict

import pandas as pd

from lab_1.util.Hypothesis import Hypothesis
from lab_1.util.decorators import measure_execution_time
from lab_1.util.constants import *

# №21
# Вопрос: Какова удовлетворенность клиентов от взаимодействия с сайтом?
# Гипотеза: Среднее количество переходов от одного пользователя больше, чем $VAL

@measure_execution_time
def compute(dataframe: pd.DataFrame, comparable_value: float) -> Tuple[str, str]:
    hypothesis: Hypothesis = Hypothesis(
        h0="Среднее количество переходов от одного пользователя больше, чем {val}",
        h1="Среднее количество переходов от одного пользователя не больше, чем {val}",
        condition=lambda x: x > comparable_value
    )

    users: Dict[str, bool] = dict()
    users_count: int = 0
    transition_count: int = 0

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[ID])
        if users.get(user_id) is None:
            users.update({user_id: True})
            users_count += 1
        transition_count += 1
    value: float = transition_count/users_count  # computed from dataframe
    return hypothesis.compute(value), f"{value}"
