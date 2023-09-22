from typing import Tuple, Dict, Callable, List

import numpy as np
import pandas as pd

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time
from lab_1.util.extensions import is_add_request


# №16
# Вопрос: Какова удовлетворенность клиентов от взаимодействия с сайтом?
# Гипотеза: Среднее количество элементов в корзине клиента равно: ...

@measure_execution_time
def compute_16(dataframe: pd.DataFrame) -> Tuple[float, str]:
    users_items: Dict[str, List[int]] = dict()

    def update_data(_user: str, _request: str) -> None:
        is_add: bool
        item_id: int
        is_add, item_id = is_add_request(_request)
        if is_add:
            if _user in users_items:
                users_items[_user].append(item_id)
            else:
                users_items.update({_user: [item_id]})

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[USER])
        url: str = str(row[ENDPOINT])
        update_data(user_id, url)

    result: float = np.array(list(map(lambda l: len(l), users_items.values()))).mean()

    return (
        result,
        f"clients_size={len(users_items.values())}; result={result}"
    )
