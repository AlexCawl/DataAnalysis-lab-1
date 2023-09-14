from typing import Tuple

import pandas as pd

from lab_1.util.Hypothesis import Hypothesis
from lab_1.util.decorators import measure_execution_time


# №6
# Вопрос: Какие есть возможности по повышению эффективности интернет-магазина?
# Гипотеза: Общее число запросов КАТАЛОГ, меньше чем ПОИСК

@measure_execution_time
def compute(dataframe: pd.DataFrame, comparable_value: float) -> Tuple[str, str]:
    hypothesis: Hypothesis = Hypothesis(
        h0="Общее число запросов КАТАЛОГ, меньше чем ПОИСК",
        h1="Общее число запросов КАТАЛОГ, не меньше чем ПОИСК",
        condition=lambda x: x > comparable_value
    )
    value: float = 2  # computed from dataframe
    return hypothesis.compute(value), f"{value}"