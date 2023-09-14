from typing import Tuple

import pandas as pd

from lab_1.util.Hypothesis import Hypothesis
from lab_1.util.decorators import measure_execution_time


# №19
# Вопрос: Какова удовлетворенность клиентов от взаимодействия с сайтом?
# Гипотеза: при формировании своей продуктовой корзины, покупатель с большей степенью воспользуется КАТАЛОГОМ, нежели ПОИСКОМ

@measure_execution_time
def compute(dataframe: pd.DataFrame, comparable_value: float) -> Tuple[str, str]:
    hypothesis: Hypothesis = Hypothesis(
        h0="при формировании своей продуктовой корзины, покупатель с большей степенью воспользуется КАТАЛОГОМ, нежели ПОИСКОМ",
        h1="при формировании своей продуктовой корзины, покупатель с большей степенью воспользуется ПОИСКОМ, нежели КАТАЛОГОМ",
        condition=lambda x: x > comparable_value
    )
    value: float = 2  # computed from dataframe
    return hypothesis.compute(value), f"{value}"