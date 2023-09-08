from typing import Tuple

import pandas as pd


# Гипотеза №2
# При добавлении предмета с использованием **КАТАЛОГА** пользователь добавляет следующий предмет в
# корзину чаще, чем при использовании **ПОИСКА**

def check_if_added_few_items_more_often_from_catalog_then_from_search(dataframe: pd.DataFrame) -> Tuple[str, str]:
    h0: str = "h0: При добавлении предмета с использованием КАТАЛОГА пользователь добавляет следующий предмет в корзину" \
              " чаще, чем при использовании ПОИСКА"
    h1: str = "h0: При добавлении предмета с использованием ПОИСКА пользователь добавляет следующий предмет в корзину" \
              "чаще, чем при использовании КАТАЛОГА"
    checked_users: dict = dict()

    def user_addbasket_count(_dataframe: pd.DataFrame, _index: int, _user_id: str) -> Tuple[int, int]:
        state: int = 0
        _catalog_counter: int = 0
        _search_counter: int = 0
        for i in range(_index, len(_dataframe)):
            _row: pd.Series = _dataframe.loc[i]
            if str(_row["ID"]) == _user_id:
                url: str = str(_row["URL"])
                if url.startswith("/catalog"):
                    state = 1
                elif url.startswith("/search"):
                    state = 2
                elif url.startswith("/addbasket"):
                    if state == 1:
                        _catalog_counter += 1
                    elif state == 2:
                        _search_counter += 1
                    state = 0
        return _catalog_counter, _search_counter

    catalogue_count: int = 0
    search_count: int = 0

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        _id = str(row["ID"])
        if checked_users.get(_id) is None:
            res: Tuple[int, int] = user_addbasket_count(dataframe, index, str(row["ID"]))
            catalogue_count += 1 if res[0] > 1 else 0
            search_count += 1 if res[1] > 1 else 0
            checked_users.update({_id: 1})
    return h0 if catalogue_count > search_count else h1, f"{catalogue_count + search_count} | " \
                                                         f"{catalogue_count} - {search_count}"
