from typing import List, Set, Dict

import pandas as pd

from labs.lab_1.util.constants import DATE_DAY_PRECISION, DATE_WEEK_PRECISION, DAY_OF_WEEK, HOUR_OF_DAY, USER, ENDPOINT, \
    DATA_OUTPUT_FOLDER
from labs.lab_1.util.extensions import is_add_request
from labs.lab_1.util.splitter import split_by_keys
from labs.util.benchmarking.measuring import measure_execution_time
from labs.util.plot.graphics import single_plot, multi_plot


# №11
# Вопрос: Какова эффективность работы службы привлечения клиентов?
# Гипотеза: Коэффициент становление клиентом из посетителя за весь период равен: ...

@measure_execution_time
def main_11(dataframe: pd.DataFrame) -> float:
    keys: List[str] = [DATE_DAY_PRECISION, DATE_WEEK_PRECISION, DAY_OF_WEEK, HOUR_OF_DAY]
    data: Dict[str, Dict[str, float]] = dict()
    for key in keys:
        values: Dict[str, float] = split_by_keys(key, dataframe, lambda frame: _compute_11(frame))
        data.update({key: values})
        single_plot(values, 11, key.lower(), DATA_OUTPUT_FOLDER)

    multi_plot(list(data[DATE_DAY_PRECISION].values()), 11, "all", DATA_OUTPUT_FOLDER)
    return _compute_11(dataframe)


def _compute_11(dataframe: pd.DataFrame) -> float:
    users: Set[str] = set()
    customers: Set[str] = set()

    for index in dataframe.index:
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[USER])
        url: str = str(row[ENDPOINT])

        if is_add_request(url):
            customers.add(user_id)
        users.add(user_id)
    return len(customers) / len(users)
