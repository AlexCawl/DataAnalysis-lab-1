from typing import Tuple, Dict
from lab_1.util.constants import *
import pandas as pd


# Гипотеза №5
# Среднее количество покупок у пользователя больше чем (Значение) (к примеру 1)

def average_purchase_count_per_user(dataframe: pd.DataFrame) -> Tuple[str, str]:
    average_purchase: int = 2
    h0: str = f"h0: Среднее количество покупок у пользователя больше чем {average_purchase}"
    h1: str = f"h1: Среднее количество покупок у пользователя меньше чем {average_purchase}"
    users_count: int = 0
    purchases: int = 0
    checked_users: Dict[str, bool] = dict()

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[ID])
        url: str = str(row[URL])
        if url.startswith(ADDBASKET):
            purchases += 1
            if checked_users.get(user_id) is None:
                users_count += 1
                checked_users[user_id] = True
    result: float = purchases / users_count
    return h0 if result > average_purchase else h1, f"{users_count} | {purchases}"
