from typing import Dict, List

import pandas as pd

from core.lab_1.util.constants import DATE_DAY_PRECISION, DATE_WEEK_PRECISION, DAY_OF_WEEK, \
    HOUR_OF_DAY, USER, ENDPOINT, DATA_OUTPUT_FOLDER
from core.lab_1.util.extensions import is_add_request, is_order_request, get_id_from_add_request
from core.lab_1.util.splitter import split_by_keys
from core.util.benchmarking.measuring import measure_execution_time
from core.util.plot.graphics import single_plot, multi_plot


# №14
# Вопрос: Какова эффективность работы службы отгрузок товаров?
# Гипотеза: Средний товарооборот за весь период равен: ...

@measure_execution_time
def main_14(dataframe: pd.DataFrame) -> float:
    keys: List[str] = [DATE_DAY_PRECISION, DATE_WEEK_PRECISION, DAY_OF_WEEK, HOUR_OF_DAY]
    data: Dict[str, Dict[str, float]] = dict()
    for key in keys:
        values: Dict[str, float] = split_by_keys(key, dataframe, lambda frame: _compute_14(frame))
        data.update({key: values})
        single_plot(values, 14, key.lower(), DATA_OUTPUT_FOLDER)

    multi_plot(list(data[DATE_DAY_PRECISION].values()), 14, "all", DATA_OUTPUT_FOLDER)
    return _compute_14(dataframe)


def _compute_14(dataframe: pd.DataFrame) -> float:
    users_items: Dict[str, List[str]] = dict()
    ordered_count: Dict[str, int] = {"ordered_count": 0}

    def update_data(_user: str, request: str) -> None:
        if is_add_request(request):
            if _user in users_items:
                users_items[_user].append(get_id_from_add_request(request))
            else:
                users_items.update({_user: [get_id_from_add_request(request)]})
        elif is_order_request(request):
            items: List[str] = users_items.get(_user, [])
            ordered_count.update({"ordered_count": ordered_count["ordered_count"] + len(items)})
            items.clear()

    for index in dataframe.index:
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[USER])
        url: str = str(row[ENDPOINT])
        update_data(user_id, url)

    return ordered_count["ordered_count"]
