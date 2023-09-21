from typing import Tuple, Dict, List, Callable, Any

import pandas as pd

from lab_1.util.decorators import measure_execution_time
from lab_1.util.constants import *


# №10
# Вопрос: Какие есть возможности по повышению эффективности интернет-магазина?
# Гипотеза: Последний запрос пользователя за сессию является ORDER, а не любой другой с вероятностью

@measure_execution_time
def compute_10(dataframe: pd.DataFrame, comparable_value: float) -> Tuple[str, str]:
    # h0: str = f"Последний запрос пользователя за сессию является ORDER, а не любой другой с вероятностью более чем {comparable_value:.2f}"
    # h1: str = f"Последний запрос пользователя за сессию является любой другой, а не ORDER с вероятностью не более чем {comparable_value:.2f}"
    # condition: Callable[[int], bool] = lambda v: v > comparable_value
    users: Dict[str, List[str]] = dict()

    def process_user(_user_id: str, _request: str) -> None:
        if _user_id in users:
            users[_user_id].append(_request)
        else:
            users.update({_user_id: [_request]})

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        process_user(row[ID], row[URL])

    orders_last_count: int = 0
    for key, value in users.items():
        if value[-1] == "/order.phtml":
            orders_last_count += 1

    return (
        f"Последний запрос пользователя за сессию является ORDER, а не любой другой с вероятностью {orders_last_count/len(users)}",
        f"orders_last_count={orders_last_count}; all={len(users)}; result={orders_last_count / len(users)}"
    )
    # return (
    #     h0 if condition(orders_last_count / len(users)) else h1,
    #     f"orders_last_count={orders_last_count}; all={len(users)}; result={orders_last_count / len(users)}"
    # )
