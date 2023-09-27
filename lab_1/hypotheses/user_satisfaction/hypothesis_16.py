from typing import Dict, List

import numpy as np
import pandas as pd

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time
from lab_1.util.extensions import is_add_request, get_id_from_add_request
from lab_1.util.graphics import single_plot, multi_plot
from lab_1.util.splitter import split_by_keys


# №16
# Вопрос: Какова удовлетворенность клиентов от взаимодействия с сайтом?
# Гипотеза: Среднее количество элементов в корзине клиента равно: ...

@measure_execution_time
def main_16(dataframe: pd.DataFrame, path: str) -> float:
    keys: List[str] = [DATE_DAY_PRECISION, DATE_WEEK_PRECISION, DAY_OF_WEEK, HOUR_OF_DAY]
    data: Dict[str, Dict[str, float]] = dict()
    for key in keys:
        values: Dict[str, float] = split_by_keys(key, dataframe, lambda frame: _compute_16(frame))
        data.update({key: values})
        single_plot(values, f"16-{key}", path)

    multi_plot(list(data[DATE_DAY_PRECISION].values()), "16-all", path)
    return _compute_16(dataframe)


def _compute_16(dataframe: pd.DataFrame) -> float:
    users_items: Dict[str, List[str]] = dict()

    def update_data(_user: str, request: str) -> None:
        if is_add_request(request):
            if _user in users_items:
                users_items[_user].append(get_id_from_add_request(request))
            else:
                users_items.update({_user: [get_id_from_add_request(request)]})

    for index in dataframe.index:
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[USER])
        url: str = str(row[ENDPOINT])
        update_data(user_id, url)

    return np.array(list(map(lambda l: len(l), users_items.values()))).mean()
