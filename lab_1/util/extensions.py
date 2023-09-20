import re
from datetime import datetime as Datetime
from re import Match
from typing import Tuple, Dict, Set, Any
from geolite2 import geolite2
import pandas as pd
import numpy as np
from lab_1.util.constants import *


def get_users_baskets(dataframe: pd.DataFrame) -> Dict[str, Set[str]]:
    result: Dict[str, Set[str]] = dict()

    def update_data(_user: str, _request: str) -> None:
        if _request.startswith(ADD_BASKET):
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


def is_add_request(request: str) -> Tuple[bool, int]:
    result: Match[str] | None = re.match(ADD_BASKET_PATTERN, request)
    if result:
        return True, int(re.compile(ADD_BASKET_PATTERN).search(request).group(1))
    else:
        return False, -1


def is_order_request(request: str) -> bool:
    return bool(re.match(ORDER_PATTERN, request))


def is_catalogue_request(request: str) -> bool:
    return bool(re.match(CATALOG_PATTERN, request))


def is_search_request(request: str) -> bool:
    return bool(re.match(SEARCH_PATTERN, request))


def parse_timestamp(timestamp: str) -> Dict[str, Any]:
    datetime_pattern: str = "%d/%b/%Y:%H:%M:%S"
    time_raw: str = timestamp.split(" ")[0]
    time: Datetime = Datetime.strptime(time_raw, datetime_pattern)
    return {
        DAY: time.day,
        MONTH: time.month,
        YEAR: time.year,
        HOUR: time.hour,
        DAY_OF_WEEK: time.weekday()
    }


_geo = geolite2.reader()


def get_county_by_ip(ip_address: str) -> str | float:
    try:
        x = _geo.get(ip_address)
    except ValueError:
        return np.nan
    try:
        return x['country']['names']['en'] if x else np.nan
    except KeyError:
        return np.nan
