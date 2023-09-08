from typing import Tuple

import pandas as pd


# Гипотеза №7
# Среднее количество переходов от одного пользователя (Значение)

def average_transition_count_per_user(dataframe: pd.DataFrame) -> Tuple[float, str]:
    hash_map: dict[str: int] = dict()
    h0: str = "Среднее количество переходов от одного пользователя равно"

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        hash_map.update({row["ID"]: hash_map.get(row["ID"], 0)+1})
    hash_sum: int = sum(hash_map.values())
    transition: float = hash_sum / len(hash_map)
    return transition, f"{h0} {transition}"
