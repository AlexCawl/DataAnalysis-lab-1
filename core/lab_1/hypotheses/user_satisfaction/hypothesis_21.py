from typing import Dict, List

import pandas as pd

from core.lab_1.util.constants import DATE_DAY_PRECISION, DATE_WEEK_PRECISION, DAY_OF_WEEK, \
    HOUR_OF_DAY, USER, DATA_OUTPUT_FOLDER
from core.lab_1.util.splitter import split_by_keys
from core.util.benchmarking.measuring import measure_execution_time
from core.util.plot.graphics import single_plot, multi_plot


# №21
# Вопрос: Какова удовлетворенность клиентов от взаимодействия с сайтом?
# Гипотеза: Среднее количество переходов от одного пользователя равно: ...

@measure_execution_time
def main_21(dataframe: pd.DataFrame) -> float:
    keys: List[str] = [DATE_DAY_PRECISION, DATE_WEEK_PRECISION, DAY_OF_WEEK, HOUR_OF_DAY]
    data: Dict[str, Dict[str, float]] = dict()
    for key in keys:
        values: Dict[str, float] = split_by_keys(key, dataframe, lambda frame: _compute_21(frame))
        data.update({key: values})
        single_plot(values, 16, key.lower(), DATA_OUTPUT_FOLDER)

    multi_plot(list(data[DATE_DAY_PRECISION].values()), 16, "all", DATA_OUTPUT_FOLDER)
    return _compute_21(dataframe)


@measure_execution_time
def _compute_21(dataframe: pd.DataFrame) -> float:
    users: Dict[str, bool] = dict()
    users_count: int = 0
    transition_count: int = 0

    for index in dataframe.index:
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[USER])
        if users.get(user_id) is None:
            users.update({user_id: True})
            users_count += 1
        transition_count += 1

    return transition_count / users_count
