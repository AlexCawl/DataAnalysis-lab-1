from typing import Tuple
from lab_1.util.constants import *
import pandas as pd


# Гипотеза №2
# При добавлении предмета с использованием КАТАЛОГА пользователь добавляет следующий предмет в
# корзину чаще, чем при использовании ПОИСКА

def check_if_added_few_items_more_often_from_catalog_then_from_search(dataframe: pd.DataFrame) -> Tuple[str, str]:
    h0: str = "h0: При добавлении предмета с использованием КАТАЛОГА пользователь добавляет следующий предмет" \
              " в корзину чаще, чем при использовании ПОИСКА"
    h1: str = "h1: При добавлении предмета с использованием ПОИСКА пользователь добавляет следующий предмет" \
              " в корзину чаще, чем при использовании КАТАЛОГА"
    users_checked_catalog: dict = dict()
    users_checked_search: dict = dict()
    users_addbasket_catalog: dict = dict()
    users_addbasket_search: dict = dict()

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

    catalogue_count: int = 0
    search_count: int = 0

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[ID])
        url: str = str(row[URL])
        if url.startswith(ADDBASKET) and (users_checked_catalog.get(user_id) is None or
                                          users_checked_search.get(user_id) is None):
            last_request: int = user_last_request(dataframe, index, user_id)
            if last_request == 0:       # catalog
                if users_addbasket_catalog.get(user_id):
                    if users_checked_catalog.get(user_id) is None:
                        catalogue_count += 1
                        users_checked_catalog[user_id] = True
                else:
                    users_addbasket_catalog[user_id] = 1
            elif last_request == 1:     # search
                if users_addbasket_search.get(user_id):
                    if users_checked_search.get(user_id) is None:
                        search_count += 1
                        users_checked_search[user_id] = True
                else:
                    users_addbasket_search[user_id] = 1
    return h0 if catalogue_count > search_count else h1, f"{catalogue_count + search_count} | " \
                                                         f"{catalogue_count} - {search_count}"
