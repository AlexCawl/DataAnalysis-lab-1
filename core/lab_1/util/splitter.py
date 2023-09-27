from typing import Dict, Callable

import pandas as pd
from pandas.core.groupby import DataFrameGroupBy


def split_by_keys(key: str, dataframe: pd.DataFrame, computer: Callable[[pd.DataFrame], float]) -> Dict[str, float]:
    result: Dict[str, float] = dict()
    groups: DataFrameGroupBy = dataframe.groupby(key)
    for fk, frame in groups:
        result.update({str(fk): computer(frame[frame[key] == fk])})
    return result
