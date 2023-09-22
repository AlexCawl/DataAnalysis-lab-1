from typing import List, Set, Dict

import pandas as pd

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time
from lab_1.util.extensions import is_add_request
from lab_1.util.graphics import single_plot, multi_plot
from lab_1.util.splitter import split_by_keys


# №11
# Вопрос: Какова эффективность работы службы привлечения клиентов?
# Гипотеза: Коэффициент становление клиентом из посетителя за период [ЧАС/ДЕНЬ/НЕДЕЛЯ/МЕСЯЦ/ВСЕ ВРЕМЯ/ДЕНЬ НЕДЕЛИ] равен: ...

@measure_execution_time
def main_11(dataframe: pd.DataFrame, path: str) -> float:
    keys: List[str] = [DATE_DAY_PRECISION, DATE_WEEK_PRECISION, DAY_OF_WEEK, HOUR_OF_DAY]
    data: Dict[str, Dict[str, float]] = dict()
    for key in keys:
        values: Dict[str, float] = split_by_keys(key, dataframe, lambda frame: _compute_11(frame))
        data.update({key: values})
        single_plot(values, f"11-{key}", path)

    all_hist_data: List[float] = []
    for key, value in data.items():
        all_hist_data.extend(value.values())
    multi_plot(all_hist_data, "11-all", path)
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
