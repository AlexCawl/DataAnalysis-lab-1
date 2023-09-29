from typing import Dict, List

import pandas as pd

from labs.lab_1.util.constants import ENDPOINT, USER
from labs.util.benchmarking.measuring import measure_execution_time


# №10
# Вопрос: Какие есть возможности по повышению эффективности интернет-магазина?
# Гипотеза: Последний запрос пользователя за сессию является ORDER, а не любой другой с вероятностью: ...

@measure_execution_time
def main_10(dataframe: pd.DataFrame) -> float:
    users: Dict[str, List[str]] = dict()

    def process_user(_user_id: str, _request: str) -> None:
        if _user_id in users:
            users[_user_id].append(_request)
        else:
            users.update({_user_id: [_request]})

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        process_user(row[USER], row[ENDPOINT])

    orders_last_count: int = 0
    for key, value in users.items():
        if value[-1] == "/order.phtml":
            orders_last_count += 1

    return orders_last_count / len(users)
