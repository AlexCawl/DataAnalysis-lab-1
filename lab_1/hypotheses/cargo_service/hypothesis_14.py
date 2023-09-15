from typing import Tuple, Dict, Callable

import pandas as pd

from lab_1.util.decorators import measure_execution_time
from lab_1.util.constants import *


# №14
# Вопрос: Какова эффективность работы службы отгрузок товаров?
# Гипотеза: Средний товарооборот за день больше, чем $VAL

@measure_execution_time
def compute(dataframe: pd.DataFrame, comparable_value: float) -> Tuple[str, str]:
    h0: str = "Средний товарооборот за день больше, чем {VAL}"
    h1: str = "Средний товарооборот за день не больше, чем {VAL}"
    condition: Callable[[int], bool] = lambda t: t > comparable_value
    # /// реализация гипотезы \\\
    result: float = 2  # computed from dataframe
    return (
        h0.format(VAL=result) if condition(result) else h1.format(VAL=result),
        f""
    )
