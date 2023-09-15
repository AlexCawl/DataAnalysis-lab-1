from typing import Tuple, Dict, Callable, List

import numpy as np
import pandas as pd

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time


# №13
# Вопрос: Какова эффективность работы службы отгрузок товаров?
# Гипотеза: Средний объем продуктовой корзины покупателя больше чем $VAL

@measure_execution_time
def compute_13(dataframe: pd.DataFrame, comparable_value: float) -> Tuple[str, str]:
    h0: str = f"Среднее значение заказываемых товаров у покупателя больше чем {comparable_value:.2f}"
    h1: str = f"Среднее значение заказываемых товаров у покупателя не больше чем {comparable_value:.2f}"
    condition: Callable[[int], bool] = lambda e: e > comparable_value

    users_items: Dict[str, List[str]] = dict()
    users_orders: List[int] = []

    def update_data(_user: str, _request: str) -> None:
        if _request.startswith(ADDBASKET):
            if _user in users_items:
                users_items[_user].append(_request)
            else:
                users_items.update({_user: [_request]})
        elif _request.startswith(ORDER):
            items: List[str] = users_items.get(_user, [])
            users_orders.append(len(items))
            items.clear()

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[ID])
        url: str = str(row[URL])
        update_data(user_id, url)

    result: float = np.array(users_orders).mean()
    return (
        h0 if condition(result) else h1,
        f"orders_size={len(users_orders)}; result={result}"
    )
