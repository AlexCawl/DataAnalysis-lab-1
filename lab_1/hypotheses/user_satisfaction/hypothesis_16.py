from typing import Tuple, Dict, Callable, List

import numpy as np
import pandas as pd

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time


# №16
# Вопрос: Какова удовлетворенность клиентов от взаимодействия с сайтом?
# Гипотеза: Среднее количество элементов в корзине клиента равно: ...

@measure_execution_time
def compute_16(dataframe: pd.DataFrame) -> Tuple[float, str]:
    users_items: Dict[str, List[str]] = dict()

    def update_data(_user: str, _request: str) -> None:
        if _request.startswith(ADD_BASKET):
            if _user in users_items:
                users_items[_user].append(_request)
            else:
                users_items.update({_user: [_request]})

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[ID])
        url: str = str(row[URL])
        update_data(user_id, url)

    result: float = np.array(list(map(lambda l: len(l), users_items.values()))).mean()

    return (
        result,
        f"clients_size={len(users_items.values())}; result={result}"
    )
