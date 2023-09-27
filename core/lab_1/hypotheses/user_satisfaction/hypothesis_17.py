from typing import Dict, List

import numpy as np
import pandas as pd

from core.lab_1.util.constants import DATE_DAY_PRECISION, DATE_WEEK_PRECISION, DAY_OF_WEEK, \
    HOUR_OF_DAY, USER, DATA_OUTPUT_FOLDER, TIMESTAMP
from core.lab_1.util.splitter import split_by_keys
from core.util.benchmarking.measuring import measure_execution_time
from core.util.plot.graphics import single_plot, multi_plot


# №17
# Вопрос: Какова удовлетворенность клиентов от взаимодействия с сайтом?
# Гипотеза: Среднее время браузинга пользователем товаров на сайте за весь период равно: ...

@measure_execution_time
def main_17(dataframe: pd.DataFrame) -> float:
    keys: List[str] = [DATE_DAY_PRECISION, DATE_WEEK_PRECISION, DAY_OF_WEEK, HOUR_OF_DAY]
    data: Dict[str, Dict[str, float]] = dict()
    for key in keys:
        values: Dict[str, float] = split_by_keys(key, dataframe, lambda frame: _compute_17(frame))
        data.update({key: values})
        single_plot(values, 17, key.lower(), DATA_OUTPUT_FOLDER)

    multi_plot(list(data[DATE_DAY_PRECISION].values()), 17, "all", DATA_OUTPUT_FOLDER)
    return _compute_17(dataframe)


def _compute_17(dataframe: pd.DataFrame) -> float:
    users: Dict[str, List[pd.Timestamp]] = dict()
    users_count: int = 0

    for index in dataframe.index:
        row: pd.Series = dataframe.loc[index]
        user: str = row[USER]
        if users.get(user) is None:
            users.update({user: [row[TIMESTAMP]]})
            users_count += 1
        else:
            users.get(user).append(row[TIMESTAMP])

    diffs: List[float] = []
    for key in users.keys():
        if len(users[key]) > 1:
            first_request: pd.Timestamp = users[key][0]
            last_request: pd.Timestamp = users[key][-1]
            diffs.append(pd.Timedelta(last_request - first_request).seconds / 60.0)
    return np.array(diffs).mean()
