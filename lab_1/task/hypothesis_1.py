from typing import Tuple

import pandas as pd

from lab_1.util.decorators import measure_execution_time


# Гипотеза №1
# При использовании КАТАЛОГА пользователь добавляет предмет в корзину чаще, чем после ПОИСКА

@measure_execution_time
def check_items_added_from_catalogue_rather_search(dataframe: pd.DataFrame, strict: bool = False) -> Tuple[str, str]:
    h0: str = "h0: При использовании КАТАЛОГА пользователь добавляет предмет в корзину чаще, чем после ПОИСКА"
    h1: str = "h1: При использовании ПОИСКА пользователь добавляет предмет в корзину чаще, чем после КАТАЛОГА"

    def user_last_request(_dataframe: pd.DataFrame, _index: int, _user_id: str) -> int:
        for i in range(_index, -1, -1):
            _row: pd.Series = _dataframe.loc[i]
            if str(_row["ID"]) == _user_id:
                url: str = str(_row["URL"])
                if url.startswith("/catalog"):
                    return 0
                elif url.startswith("/search"):
                    return 1
        return -1

    catalogue_count: int = 0
    search_count: int = 0
    items_chosen_count: int = 0

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        if str(row["HTTP_TYPE"]) == "GET" and str(row["URL"]).startswith("/addbasket"):
            items_chosen_count += 1
            added_from: int = user_last_request(dataframe, index, str(row["ID"]))
            if added_from == 0:
                catalogue_count += 1
            elif added_from == 1:
                search_count += 1
            else:
                if strict:
                    raise Exception
                else:
                    print("----------------------------------------")
                    print(row.to_string())
                    print("Previous page is not found!")
                    print("----------------------------------------", end="\n\n")

    return h0 if catalogue_count > search_count else h1, f"{items_chosen_count} | {catalogue_count} - {search_count}"
