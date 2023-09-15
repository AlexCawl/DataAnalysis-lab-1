import enum
from typing import Tuple, Dict, List

import pandas as pd


class User(enum.Enum):
    visitor = 0
    client = 1
    customer = 2


def get_ratio(dataframe: pd.DataFrame, group1: User, group2: User) -> Tuple[float, int, int]:
    # TODO
    return 0, 0, 0


def get_items_clusters(dataframe: pd.DataFrame) -> Dict[str, List[str]]:
    # TODO
    return {}
