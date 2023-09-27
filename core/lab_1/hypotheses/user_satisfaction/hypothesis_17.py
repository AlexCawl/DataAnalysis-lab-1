from datetime import datetime as Datetime
from typing import Dict, List

import pandas as pd

from core.util.benchmarking.measuring import measure_execution_time
from core.util.plot.graphics import single_plot, multi_plot
from core.lab_1.util.splitter import split_by_keys


# №17
# Вопрос: Какова удовлетворенность клиентов от взаимодействия с сайтом?
# Гипотеза: Среднее время браузинга товаров на сайте равно: ...

@measure_execution_time
def main_17(dataframe: pd.DataFrame, path: str) -> float:
    keys: List[str] = [DATE_DAY_PRECISION, DATE_WEEK_PRECISION, DAY_OF_WEEK, HOUR_OF_DAY]
    data: Dict[str, Dict[str, float]] = dict()
    for key in keys:
        values: Dict[str, float] = split_by_keys(key, dataframe, lambda frame: _compute_17(frame))
        data.update({key: values})
        single_plot(values, f"17-{key}", path)

    multi_plot(list(data[DATE_DAY_PRECISION].values()), "17-all", path)
    return _compute_17(dataframe)


@measure_execution_time
def _compute_17(dataframe: pd.DataFrame) -> float:
    users: Dict[str, List[pd.Timestamp]] = dict()
    users_count: int = 0

    for index in dataframe.index:
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[USER])
        if users.get(user_id) is None:
            users.update({user_id: [row[DATETIME]]})
            users_count += 1
        else:
            list_to_update: List[pd.Timestamp] = users[user_id]
            if len(users[user_id]) == 1:
                list_to_update.append(row[DATETIME])
                users.update({user_id: list_to_update})
            else:
                list_to_update[1] = row[DATETIME]
                users.update({user_id: list_to_update})

    total_difference: float = 0
    for key in users.keys():
        if len(users[key]) > 1:
            first_request: Datetime = users[key][0].to_pydatetime()
            last_request: Datetime = users[key][0].to_pydatetime()
            local_difference: float = (last_request - first_request).total_seconds() / 60
            total_difference += local_difference

    return total_difference / users_count
