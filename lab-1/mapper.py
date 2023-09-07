from typing import Any

import pandas as pd
from typing import List

from LogDTO import LogDTO
from constants import *


def map_logs_to_dataframe(logs: List[LogDTO]) -> pd.DataFrame:
    dataframe: pd.DataFrame = pd.DataFrame(columns=[ID, IP_ADDRESS, DATETIME, HTTP_TYPE, HTTP_CODE, URL])
    for index, log in enumerate(logs):
        print(index)
        dataframe.loc[index] = map_log_dto_to_values(log)
        if index == 5000: break
    return dataframe


def map_log_dto_to_values(log: LogDTO) -> List[Any]:
    return [
        log.user_id,
        log.ip,
        log.date_time,
        log.http_type,
        log.code,
        log.url
    ]
