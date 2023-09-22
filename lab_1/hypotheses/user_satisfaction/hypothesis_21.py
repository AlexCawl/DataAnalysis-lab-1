from typing import Tuple, Dict, Callable, List

import pandas as pd

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time
from lab_1.util.graphics import single_plot, multi_plot
from lab_1.util.splitter import split_by_keys


# №21
# Вопрос: Какова удовлетворенность клиентов от взаимодействия с сайтом?
# Гипотеза: Среднее количество переходов от одного пользователя равно: ...

@measure_execution_time
def main_21(dataframe: pd.DataFrame, path: str) -> float:
    keys: List[str] = [DATE_DAY_PRECISION, DATE_WEEK_PRECISION, DAY_OF_WEEK, HOUR_OF_DAY]
    data: Dict[str, Dict[str, float]] = dict()
    for key in keys:
        values: Dict[str, float] = split_by_keys(key, dataframe, lambda frame: _compute_21(frame))
        data.update({key: values})
        single_plot(values, f"21-{key}", path)

    multi_plot(list(data[DATE_DAY_PRECISION].values()), "21-all", path)
    return _compute_21(dataframe)


@measure_execution_time
def _compute_21(dataframe: pd.DataFrame) -> float:
    users: Dict[str, bool] = dict()
    users_count: int = 0
    transition_count: int = 0

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[USER])
        if users.get(user_id) is None:
            users.update({user_id: True})
            users_count += 1
        transition_count += 1

    return transition_count / users_count
