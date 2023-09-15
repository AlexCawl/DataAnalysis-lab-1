from datetime import datetime as Datetime
from typing import Tuple, Dict, List, Callable

import pandas as pd

from lab_1.util.constants import *
from lab_1.util.decorators import measure_execution_time


# №17
# Вопрос: Какова удовлетворенность клиентов от взаимодействия с сайтом?
# Гипотеза: Среднее время браузинга товаров на сайте больше чем $VAL минут

@measure_execution_time
def compute(dataframe: pd.DataFrame, comparable_value: float) -> Tuple[str, str]:
    h0: str = "Среднее время браузинга товаров на сайте больше чем {VAL} минут"
    h1: str = "Среднее время браузинга товаров на сайте не больше чем {VAL} минут"
    condition: Callable[[int], bool] = lambda t: t > comparable_value
    users: Dict[str, List[str]] = dict()
    users_count: int = 0

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[ID])
        request_time: str = str(row[DATETIME])[:19]  # TODO какой 19???
        if users.get(user_id) is None:
            users.update({user_id: [request_time]})
            users_count += 1
        else:
            list_to_update: List[str] = users[user_id]
            if len(users[user_id]) == 1:
                list_to_update.append(request_time)
                users.update({user_id: list_to_update})
            else:
                list_to_update[1] = request_time
                users.update({user_id: list_to_update})

    total_difference: float = 0
    for key in users.keys():
        if len(users[key]) > 1:
            first_request: Datetime = Datetime.strptime(users[key][0], "%d/%b/%Y:%H:%M:%S")
            last_request: Datetime = Datetime.strptime(users[key][1], "%d/%b/%Y:%H:%M:%S")
            local_difference: float = (last_request - first_request).total_seconds() / 60
            total_difference += local_difference

    result: float = total_difference / users_count
    return (
        h0.format(VAL=result) if condition(result) else h1.format(VAL=result),
        f"result={result}"
    )
