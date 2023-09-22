from typing import Any, Dict
from typing import List

import pandas as pd

from .LogDTO import LogDTO
from .constants import *
from .decorators import measure_execution_time
from .extensions import parse_timestamp, get_county_by_ip


@measure_execution_time
def map_logs_to_dataframe(logs: List[LogDTO], size: int = -1) -> pd.DataFrame:
    content: List[pd.Series] = []
    for index, log in enumerate(logs):
        content.append(pd.Series(map_log_dto_to_values(log)))
        if index == size:
            break
    dataframe: pd.DataFrame = pd.concat(content, axis=1).transpose()
    return dataframe


def map_log_dto_to_values(log: LogDTO) -> Dict[str, Any]:
    return {
        USER: log.user_id,
        COUNTRY: get_county_by_ip(log.ip),
        ENDPOINT: log.url,
        TIMESTAMP: parse_timestamp(log.date_time)
    }


@measure_execution_time
def prepare_dataframe(dframe: pd.DataFrame) -> pd.DataFrame:
    dframe = dframe.astype({USER: 'string', COUNTRY: 'string', ENDPOINT: 'string'})
    dframe[TIMESTAMP] = pd.to_datetime(dframe[TIMESTAMP])
    dframe[DATE_DAY_PRECISION] = dframe.apply(lambda row: int(row[TIMESTAMP].dayofyear), axis=1)
    dframe[DATE_WEEK_PRECISION] = dframe.apply(lambda row: int(row[TIMESTAMP].weekofyear), axis=1)
    dframe[DATE_MONTH_PRECISION] = dframe.apply(lambda row: int(row[TIMESTAMP].month), axis=1)
    dframe[HOUR_OF_DAY] = dframe.apply(lambda row: int(row[TIMESTAMP].hour), axis=1)
    dframe[DAY_OF_WEEK] = dframe.apply(lambda row: int(row[TIMESTAMP].dayofweek), axis=1)
    return dframe
