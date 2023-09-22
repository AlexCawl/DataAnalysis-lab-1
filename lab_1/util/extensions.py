import re
from datetime import datetime as Datetime
from typing import Dict, Set, Any

import numpy as np
import pandas as pd
from geolite2 import geolite2

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


def is_add_request(request: str) -> bool:
    return request.startswith("/addbasket")


def get_id_from_add_request(request: str) -> str:
    return re.compile(ADD_BASKET_PATTERN).search(request).group(1)


def is_order_request(request: str) -> bool:
    return request == "/order.phtml"


def is_catalogue_request(request: str) -> bool:
    return request == "/catalog.phtml"


def is_search_request(request: str) -> bool:
    return bool(re.match(SEARCH_PATTERN, request))


def parse_timestamp(timestamp: str) -> pd.Timestamp:
    datetime_pattern: str = "%d/%b/%Y:%H:%M:%S"
    time_raw: str = timestamp.split(" ")[0]
    time: Datetime = Datetime.strptime(time_raw, datetime_pattern)
    return pd.Timestamp(
        year=time.year, month=time.month, day=time.day, hour=time.hour, minute=time.minute, second=time.second
    )


_geo = geolite2.reader()


def get_county_by_ip(ip_address: str) -> Any:
    try:
        x = _geo.get(ip_address)
    except ValueError:
        return np.nan
    try:
        return x['country']['names']['en'] if x else np.nan
    except KeyError:
        return np.nan
