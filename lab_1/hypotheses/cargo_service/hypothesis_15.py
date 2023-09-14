from typing import Tuple

import pandas as pd

from lab_1.util.Hypothesis import Hypothesis
from lab_1.util.decorators import measure_execution_time


# №15
# Вопрос: Какова эффективность работы службы отгрузок товаров?
# Гипотеза: Среднее значение заказываемых товаров у покупателя меньше, чем $VAL

@measure_execution_time
def compute(dataframe: pd.DataFrame, comparable_value: float) -> Tuple[str, str]:
    hypothesis: Hypothesis = Hypothesis(
        h0="Среднее значение заказываемых товаров у покупателя меньше, чем {val}",
        h1="Среднее значение заказываемых товаров у покупателя не меньше, чем {val}",
        condition=lambda x: x > comparable_value
    )
    value: float = 2  # computed from dataframe
    return hypothesis.compute(value), f"{value}"