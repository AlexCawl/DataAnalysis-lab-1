from typing import Dict, List

import pandas as pd

from labs.lab_1.util.constants import DATE_DAY_PRECISION, DATE_WEEK_PRECISION, DAY_OF_WEEK, HOUR_OF_DAY, USER
from labs.lab_1.util.splitter import split_by_keys
from labs.util.benchmarking.measuring import measure_execution_time
from labs.util.plot.graphics import single_plot, multi_plot


# №12
# Вопрос: Какова эффективность работы службы привлечения клиентов?
# Гипотеза: Число посетителей за весь период равно: ...


@measure_execution_time
def main_12(dataframe: pd.DataFrame) -> float:
    keys: List[str] = [DATE_DAY_PRECISION, DATE_WEEK_PRECISION, DAY_OF_WEEK, HOUR_OF_DAY]
    data: Dict[str, Dict[str, float]] = dict()
    for key in keys:
        values: Dict[str, float] = split_by_keys(key, dataframe, lambda frame: _compute_12(frame))
        data.update({key: values})
        single_plot(values, 12, key.lower())

    multi_plot(list(data[DATE_DAY_PRECISION].values()), 12, "all")
    return _compute_12(dataframe)


def _compute_12(dataframe: pd.DataFrame) -> float:
    return dataframe.groupby(USER).ngroups
