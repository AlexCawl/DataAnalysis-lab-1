from typing import Dict, List

import pandas as pd

from core.lab_1.util.constants import DATA_OUTPUT_FOLDER, DATE_DAY_PRECISION, DATE_WEEK_PRECISION, DAY_OF_WEEK, \
    HOUR_OF_DAY, USER
from core.lab_1.util.splitter import split_by_keys
from core.util.benchmarking.measuring import measure_execution_time
from core.util.plot.graphics import single_plot, multi_plot


# №12
# Вопрос: Какова эффективность работы службы привлечения клиентов?
# Гипотеза: Среднее число посетителей равно: ...


@measure_execution_time
def main_12(dataframe: pd.DataFrame) -> float:
    keys: List[str] = [DATE_DAY_PRECISION, DATE_WEEK_PRECISION, DAY_OF_WEEK, HOUR_OF_DAY]
    data: Dict[str, Dict[str, float]] = dict()
    for key in keys:
        values: Dict[str, float] = split_by_keys(key, dataframe, lambda frame: _compute_12(frame))
        data.update({key: values})
        single_plot(values, 12, key.lower(), DATA_OUTPUT_FOLDER)

    multi_plot(list(data[DATE_DAY_PRECISION].values()), 12, "all", DATA_OUTPUT_FOLDER)
    return _compute_12(dataframe)


def _compute_12(dataframe: pd.DataFrame) -> float:
    return dataframe.groupby(USER).ngroups
