import enum
from typing import Tuple, Dict, List, Set

import pandas as pd

from lab_1.util.constants import *


class User(enum.Enum):
    visitor = 0
    client = 1
    customer = 2


def get_ratio(dataframe: pd.DataFrame, group1: User, group2: User) -> Tuple[float, int, int]:
    # TODO
    return 0, 0, 0


def get_users_baskets(dataframe: pd.DataFrame) -> Dict[str, Set[str]]:
    result: Dict[str, Set[str]] = dict()

    def update_data(_user: str, _request: str) -> None:
        if _request.startswith(ADDBASKET):
            if _user in result:
                result[_user].add(_request[25:])
            else:
                result.update({_user: set(_request[25:])})

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[ID])
        url: str = str(row[URL])
        update_data(user_id, url)

    return result
