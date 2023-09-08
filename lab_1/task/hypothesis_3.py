from typing import Tuple, Dict
from lab_1.util.constants import *
import pandas as pd


# Гипотеза №3
# При добавлении предмета с использованием ПОИСКА, пользователь чаще не добавляет других предметов в корзину

def check_if_item_added_from_search_it_is_single(dataframe: pd.DataFrame) -> Tuple[str, str]:
    h0: str = "h0: При добавлении предмета с использованием ПОИСКА, пользователь чаще не добавляет" \
              " других предметов в корзину"
    h1: str = "h1: При добавлении предмета с использованием ПОИСКА, пользователь чаще добавляет" \
              " другие предметы в корзину"

    users_checked_search: Dict[str, bool] = dict()
    users_addbasket_search: Dict[str, int] = dict()

    def user_last_request(_dataframe: pd.DataFrame, _index: int, _user_id: str) -> int:
        for i in range(_index, -1, -1):
            _row: pd.Series = _dataframe.loc[i]
            if str(_row[ID]) == _user_id:
                _url: str = str(_row[URL])
                if _url.startswith(CATALOG):
                    return 0
                elif _url.startswith(SEARCH):
                    return 1
        return -1

    few_addbasket: int = 0
    users_addbasket: int = 0
    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[ID])
        url: str = str(row[URL])
        if url.startswith(ADDBASKET):
            if users_addbasket_search.get(user_id) and users_checked_search.get(user_id) is None:
                users_checked_search[user_id] = True
                few_addbasket += 1
                continue

            last_request: int = user_last_request(dataframe, index, user_id)
            if last_request == 1:   # search
                if users_addbasket_search.get(user_id) is None:
                    users_addbasket_search[user_id] = 1
                    users_addbasket += 1
    return h0 if few_addbasket*2 < users_addbasket else h1, f"{users_addbasket} | {few_addbasket}"
