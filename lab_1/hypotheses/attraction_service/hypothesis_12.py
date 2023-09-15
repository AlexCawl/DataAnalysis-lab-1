from typing import Tuple, Callable, Dict, List

import pandas as pd

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time


# №12
# Вопрос: Какова эффективность работы службы привлечения клиентов?
# Гипотеза: Среднее число посетителей за день больше, чем $VAL

@measure_execution_time
def compute(dataframe: pd.DataFrame, comparable_value: float) -> Tuple[str, str]:
    h0: str = f"Среднее число посетителей за день больше, чем {comparable_value:.2f}"
    h1: str = f"Среднее число посетителей за день не больше, чем {comparable_value:.2f}"
    condition: Callable[[int], bool] = lambda x: x > comparable_value
    visitors: Dict[str, List[str]] = dict()
    unique_visitors: int = 0

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[ID])
        _date: str = str(row[DATETIME])[:10]

        if _date not in visitors.keys():
            visitors.update({_date: []})

        if user_id not in visitors[_date]:
            visitors[_date].append(user_id)

    overall_sum: int = 0

    for amount_of_users in visitors.values():
        sum_for_day: int = len(amount_of_users)
        overall_sum += sum_for_day

    result: float = overall_sum / len(visitors)
    return (
        h0 if condition(result) else h1,
        f"overall_sum={overall_sum}; visitors_count={len(visitors)}; result={result}"
    )
