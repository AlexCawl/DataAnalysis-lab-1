from typing import Tuple, Callable, Set

import pandas as pd

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time


# №11
# Вопрос: Какова эффективность работы службы привлечения клиентов?
# Гипотеза: Коэффициент становление клиентом из посетителя больше $VAL

@measure_execution_time
def compute_11(dataframe: pd.DataFrame, comparable_value: float) -> Tuple[str, str]:
    h0: str = f"Коэффициент становление клиентом из посетителя больше чем {comparable_value:.2f}"
    h1: str = f"Коэффициент становление клиентом из посетителя не больше чем {comparable_value:.2f}"
    condition: Callable[[int], bool] = lambda k: k > comparable_value

    users: Set[str] = set()
    customers: Set[str] = set()

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[ID])
        url: str = str(row[URL])

        if url.startswith(ADDBASKET):
            customers.add(user_id)
        users.add(user_id)

    result: float = len(customers) / len(users)
    return (
        h0 if condition(result) else h1,
        f"customers_size={len(customers)}; users_size={len(users)}"
    )
