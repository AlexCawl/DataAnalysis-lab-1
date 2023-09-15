from typing import Tuple, Dict, Callable

import pandas as pd

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time


# №21
# Вопрос: Какова удовлетворенность клиентов от взаимодействия с сайтом?
# Гипотеза: Среднее количество переходов от одного пользователя больше, чем $VAL

@measure_execution_time
def compute(dataframe: pd.DataFrame, comparable_value: float) -> Tuple[str, str]:
    h0: str = "Среднее количество переходов от одного пользователя больше, чем {VAL}"
    h1: str = "Среднее количество переходов от одного пользователя не больше, чем {VAL}"
    condition: Callable[[int], bool] = lambda t: t > comparable_value
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

    result: float = transition_count / users_count
    return (
        h0.format(VAL=result) if condition(result) else h1.format(VAL=result),
        f"transition_count={transition_count}; users_count={users_count}; result={result}"
    )
