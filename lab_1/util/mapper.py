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
