from typing import Tuple, Dict, Callable, List

import numpy as np
import pandas as pd

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time


# №14
# Вопрос: Какова эффективность работы службы отгрузок товаров?
# Гипотеза: Средний товарооборот за день равен: ...

@measure_execution_time
def compute_14(dataframe: pd.DataFrame) -> Tuple[float, str]:
    users_items: Dict[str, List[str]] = dict()
    orders_per_day: Dict[str, int] = dict()

    def update_data(_user: str, _request: str, _datetime: str) -> None:
        if _request.startswith(ADD_BASKET):
            if _user in users_items:
                users_items[_user].append(_request)
            else:
                users_items.update({_user: [_request]})
        elif _request.startswith(ORDER):
            items: List[str] = users_items.get(_user, [])
            orders_per_day.update({_datetime: orders_per_day.get(_datetime, 0) + len(items)})
            items.clear()

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[ID])
        url: str = str(row[URL])
        datetime: str = str(row[DATETIME])[:10]
        update_data(user_id, url, datetime)

    result: float = np.array(list(orders_per_day.values())).mean()
    return (
        result,
        f"days={len(orders_per_day.values())}; result={result}"
    )
