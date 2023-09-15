from typing import Tuple, Dict, Callable, Set

import pandas as pd

from lab_1.util.decorators import measure_execution_time
from lab_1.util.constants import *


# №11
# Вопрос: Какова эффективность работы службы привлечения клиентов?
# Гипотеза: Коэффициент становление клиентом из посетителя больше $VAL

@measure_execution_time
def compute(dataframe: pd.DataFrame, comparable_value: float) -> Tuple[str, str]:
    h0: str = "Коэффициент становление клиентом из посетителя больше, чем {VAL}"
    h1: str = "Коэффициент становление клиентом из посетителя не больше, чем {VAL}"
    condition: Callable[[int], bool] = lambda t: t > comparable_value

    users: Set[str] = set()
    customers: Set[str] = set()

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[ID])
        url: str = str(row[URL])

        if url.startswith(ADDBASKET):
            customers.add(user_id)
        users.add(user_id)
    # TODO поправить вывод гипотезы
    result: float = len(customers) / len(users)  # computed from dataframe
    return (
        h0.format(VAL=result) if condition(result) else h1.format(VAL=result),
        f""
    )
