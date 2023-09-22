from typing import Tuple, Dict, List

import numpy as np
import pandas as pd

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time
from lab_1.util.extensions import is_order_request


# №13
# Вопрос: Какова эффективность работы службы отгрузок товаров?
# Гипотеза: Средний объем продуктовой корзины покупателя равен: ...

@measure_execution_time
def compute_13(dataframe: pd.DataFrame) -> Tuple[float, str]:
    users_items: Dict[str, List[str]] = dict()
    users_orders: List[int] = []

    def update_data(_user: str, _request: str) -> None:
        if _request.startswith(ADD_BASKET):
            if _user in users_items:
                users_items[_user].append(_request)
            else:
                users_items.update({_user: [_request]})
        elif is_order_request(_request):
            items: List[str] = users_items.get(_user, [])
            users_orders.append(len(items))
            items.clear()

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[USER])
        url: str = str(row[ENDPOINT])
        update_data(user_id, url)

    result: float = np.array(users_orders).mean()
    return (
        result,
        f"orders_size={len(users_orders)}; result={result}"
    )
