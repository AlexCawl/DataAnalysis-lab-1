from typing import Tuple

import pandas as pd

from lab_1.util.Hypothesis import Hypothesis
from lab_1.util.decorators import measure_execution_time


# №10
# Вопрос: Какие есть возможности по повышению эффективности интернет-магазина?
# Гипотеза: Последний запрос пользователя за сессию является ORDER, а не любой другой

@measure_execution_time
def compute(dataframe: pd.DataFrame, comparable_value: float) -> Tuple[str, str]:
    hypothesis: Hypothesis = Hypothesis(
        h0="Последний запрос пользователя за сессию является ORDER, а не любой другой",
        h1="Последний запрос пользователя за сессию является любой другой, а не ORDER",
        condition=lambda x: x > comparable_value
    )
    value: float = 2  # computed from dataframe
    return hypothesis.compute(value), f"{value}"