import pandas as pd
import LogDTO
from constants import *


def map_logs_to_dataframe(logs: list[LogDTO]) -> pd.DataFrame:
    return pd.DataFrame(columns=[ID, IP_ADDRESS, ])
