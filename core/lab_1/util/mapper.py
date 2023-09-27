from typing import Dict
from typing import List

import pandas as pd

from core.util.benchmarking.measuring import measure_execution_time
from .constants import *
from .extensions import parse_timestamp, get_county_by_ip


@measure_execution_time
def map_tokens_to_dataframe(logs: List[Dict[str, str]], size: int = -1) -> pd.DataFrame:
    content: List[pd.Series] = []
    for index, log in enumerate(logs):
        content.append(map_tokens_to_series(log))
        if index == size:
            break
    dataframe: pd.DataFrame = pd.concat(content, axis=1).transpose()
    dataframe = dataframe.astype({USER: 'string', COUNTRY: 'string', ENDPOINT: 'string'})
    dataframe[TIMESTAMP] = pd.to_datetime(dataframe[TIMESTAMP])
    dataframe[DATE_DAY_PRECISION] = dataframe.apply(lambda row: int(row[TIMESTAMP].dayofyear), axis=1)
    dataframe[DATE_WEEK_PRECISION] = dataframe.apply(lambda row: int(row[TIMESTAMP].weekofyear), axis=1)
    dataframe[DATE_MONTH_PRECISION] = dataframe.apply(lambda row: int(row[TIMESTAMP].month), axis=1)
    dataframe[HOUR_OF_DAY] = dataframe.apply(lambda row: int(row[TIMESTAMP].hour), axis=1)
    dataframe[DAY_OF_WEEK] = dataframe.apply(lambda row: int(row[TIMESTAMP].dayofweek), axis=1)
    return dataframe


def map_tokens_to_series(log: Dict[str, str]) -> pd.Series:
    return pd.Series(
        {
            USER: log[ID],
            COUNTRY: get_county_by_ip(log[IP_ADDRESS]),
            ENDPOINT: log[URL],
            TIMESTAMP: parse_timestamp(log[DATETIME])
        }
    )
