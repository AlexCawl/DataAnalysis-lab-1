from typing import Tuple

import pandas as pd

from lab_1.util.Hypothesis import Hypothesis
from lab_1.util.decorators import measure_execution_time
from lab_1.util.constants import *


# №12
# Вопрос: Какова эффективность работы службы привлечения клиентов?
# Гипотеза: Среднее число посетителей за день больше, чем $VAL

@measure_execution_time
def compute(dataframe: pd.DataFrame, comparable_value: float) -> Tuple[str, str]:
    hypothesis: Hypothesis = Hypothesis(
        h0="Среднее число посетителей за день больше, чем {val}",
        h1="Среднее число посетителей за день не больше, чем {val}",
        condition=lambda x: x > comparable_value
    )

    visitors_per_day: dict[str: list[str]] = dict()
    counter_unique_visitors: int = 0

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[ID])
        _date: str = str(row[DATETIME])[:10]

        if _date not in visitors_per_day.keys():
            visitors_per_day.update({_date: []})

        if user_id not in visitors_per_day[_date]:
            visitors_per_day[_date].append(user_id)

    overall_sum: int = 0

    for amount_of_users in visitors_per_day.values():
        sum_for_day: int = len(amount_of_users)
        overall_sum += sum_for_day

    value: float = overall_sum / len(visitors_per_day)  # computed from dataframe
    return hypothesis.compute(value), f"{value}"
