from typing import Tuple

import pandas as pd
import numpy as np

# Гипотеза №8
# Пользователь при использовании КАТАЛОГА, после этого чаще переходит в ПОИСК


def count_catalogue_and_search_usage(dataframe: pd.DataFrame) -> tuple[str, str]:
    h0: str = "Пользователь при использовании КАТАЛОГА, после этого чаще переходит в ПОИСК"
    h1: str = "Пользователь при использовании ПОИСКА, после этого чаще переходит в КАТАЛОГ"

    hash_map: dict[str: np.array([int, int])] = dict()

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        if row["URL"].startswith("/search"):
            hash_map.update({row["ID"]: hash_map.get(row["ID"], np.array([0, 0])) + np.array([0, 1])})
        elif row["URL"].startswith("/catalog"):
            hash_map.update({row["ID"]: hash_map.get(row["ID"], np.array([0, 0])) + np.array([1, 0])})

    catalog_count: int = 0
    search_count: int = 0

    for key in hash_map.values():
        if key[0] > key[1]:
            catalog_count += 1
        else:
            search_count += 1

    return h0 if search_count > catalog_count else h1, f"catalog - {catalog_count} | search - {search_count}"
