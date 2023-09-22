from typing import Dict, List

import numpy as np
import pandas as pd

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time
from lab_1.util.extensions import is_order_request
from lab_1.util.graphics import single_plot, multi_plot
from lab_1.util.splitter import split_by_keys


# №13
# Вопрос: Какова эффективность работы службы отгрузок товаров?
# Гипотеза: Средний объем продуктовой корзины покупателя равен: ...

@measure_execution_time
def main_13(dataframe: pd.DataFrame, path: str) -> float:
    keys: List[str] = [DATE_DAY_PRECISION, DATE_WEEK_PRECISION, DAY_OF_WEEK, HOUR_OF_DAY]
    data: Dict[str, Dict[str, float]] = dict()
    for key in keys:
        values: Dict[str, float] = split_by_keys(key, dataframe, lambda frame: _compute_13(frame))
        data.update({key: values})
        single_plot(values, f"13-{key}", path)

    multi_plot(list(data[DATE_DAY_PRECISION].values()), "13-all", path)
    return _compute_13(dataframe)


def _compute_13(dataframe: pd.DataFrame) -> float:
    users_items: Dict[str, List[str]] = dict()
    users_orders: List[int] = []

    def update_data(_user: str, _request: str) -> None:
        if _request.startswith(ADD_BASKET):
            if _user in users_items:
                users_items[_user].append(_request)
            else:
                users_items.update({_user: [_request]})
        elif is_order_request(_request):
            items: List[str] = users_items.get(_user, [])
            users_orders.append(len(items))
            items.clear()

    for index in dataframe.index:
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[USER])
        url: str = str(row[ENDPOINT])
        update_data(user_id, url)

    return np.array(users_orders).mean()
