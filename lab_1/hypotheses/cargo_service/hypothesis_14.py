from typing import Tuple, Dict, List

import numpy as np
import pandas as pd

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time
from lab_1.util.extensions import is_add_request, is_order_request


# №14
# Вопрос: Какова эффективность работы службы отгрузок товаров?
# Гипотеза: Средний товарооборот за день равен: ...

@measure_execution_time
def compute_14(dataframe: pd.DataFrame) -> Tuple[float, str]:
    users_items: Dict[str, List[int]] = dict()
    orders_per_day: Dict[str, int] = dict()

    def update_data(_user: str, request: str, _datetime: str) -> None:
        is_add: bool
        item_id: int
        is_add, item_id = is_add_request(request)
        if is_add:
            if _user in users_items:
                users_items[_user].append(item_id)
            else:
                users_items.update({_user: [item_id]})
        elif is_order_request(request):
            items: List[str] = users_items.get(_user, [])
            orders_per_day.update({_datetime: orders_per_day.get(_datetime, 0) + len(items)})
            items.clear()

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[USER])
        url: str = str(row[ENDPOINT])
        datetime: str = f"{row[DAY]}#{row[MONTH]}#{row[YEAR]}"
        update_data(user_id, url, datetime)

    result: float = np.array(list(orders_per_day.values())).mean()
    return (
        result,
        f"days={len(orders_per_day.values())}; result={result}"
    )
