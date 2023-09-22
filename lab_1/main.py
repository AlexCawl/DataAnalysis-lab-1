import os
from typing import Tuple, List

import pandas as pd

from lab_1.hypotheses.attraction_service import hypothesis_11, hypothesis_12
from util.LogDTO import LogDTO
from util.decorators import measure_execution_time
from util.loader import load_logs_from_file, load_from_csv, save_to_csv
from util.mapper import map_logs_to_dataframe, prepare_dataframe


@measure_execution_time
def check_hypotheses(_dataframe: pd.DataFrame):
    hypothesis_11.main_11(dataframe, "data")
    hypothesis_12.main_12(dataframe, "data")


LOGS_PATH: str = "data/access.log"
DATAFRAME_PATH: str = "data/logs.csv"

if __name__ == '__main__':
    dataframe: pd.DataFrame
    if os.path.isfile(DATAFRAME_PATH):
        dataframe = load_from_csv(DATAFRAME_PATH)
    elif os.path.isfile(LOGS_PATH):
        logs: Tuple[List[LogDTO], int] = load_logs_from_file(LOGS_PATH)
        dataframe = map_logs_to_dataframe(logs[0])
        save_to_csv(DATAFRAME_PATH, dataframe)
    else:
        raise Exception("No .log files in ../data")
    dataframe = prepare_dataframe(dataframe)
    hypothesis_11.main_11(dataframe, "data")
    hypothesis_12.main_12(dataframe, "data")
    # check_hypotheses(df)
