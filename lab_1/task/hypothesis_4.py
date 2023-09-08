from typing import Dict, Tuple
from lab_1.util.constants import *
import pandas as pd


# Гипотеза №4
# При покупке предмета (ID предмета), также покупают (ID предмета)

def check_item_chosen_clusters(dataframe: pd.DataFrame) -> Tuple[str, str]:
    item_to_compare_first: int = 73
    item_to_compare_second: int = 6
    h0: str = f"h0: При покупке предмета {item_to_compare_first}, также покупают {item_to_compare_second}"
    h1: str = f"h1: При покупке предмета {item_to_compare_first}, редко покупают {item_to_compare_second}"

    users_items: Dict[str, int] = dict()
    items: int = 0
    both_items: int = 0
    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[ID])
        url: str = str(row[URL])
        if url.startswith(ADDBASKET):
            item_id: int = int(url.split("?")[1].split("=")[1])
            if users_items.get(user_id) is None:
                if item_id == item_to_compare_first or item_id == item_to_compare_second:
                    users_items[user_id] = item_id
                    items += 1
            else:
                if users_items[user_id] == item_to_compare_first:
                    if item_id == item_to_compare_second:
                        both_items += 1
                        users_items.pop(user_id)
    return h0 if both_items*2 > items else h1, f"{items} | {both_items}"
