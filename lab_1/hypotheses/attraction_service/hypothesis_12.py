from typing import Dict, List

import pandas as pd

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time
from lab_1.util.graphics import single_plot, multi_plot
from lab_1.util.splitter import split_by_keys


# №12
# Вопрос: Какова эффективность работы службы привлечения клиентов?
# Гипотеза: Среднее число посетителей за период [ДЕНЬ/НЕДЕЛЯ/МЕСЯЦ/ВСЕ ВРЕМЯ/ДЕНЬ НЕДЕЛИ] равно: ...


@measure_execution_time
def main_12(dataframe: pd.DataFrame, path: str) -> float:
    keys: List[str] = [DATE_DAY_PRECISION, DATE_WEEK_PRECISION, DAY_OF_WEEK, HOUR_OF_DAY]
    data: Dict[str, Dict[str, float]] = dict()
    for key in keys:
        values: Dict[str, float] = split_by_keys(key, dataframe, lambda frame: _compute_12(frame))
        data.update({key: values})
        single_plot(values, f"12-{key}", path)

    multi_plot(list(data[DATE_DAY_PRECISION].values()), "12-all", path)
    return _compute_12(dataframe)


def _compute_12(dataframe: pd.DataFrame) -> float:
    return dataframe.groupby(USER).ngroups
