import os
from typing import List, Dict

import pandas as pd

from labs.lab_1.checker import check_hypotheses
from labs.lab_1.util.constants import DATA_OUTPUT_FOLDER, LOG_CSV_FILE
from labs.lab_1.util.loader import load_logs_from_file
from labs.lab_1.util.mapper import map_tokens_to_dataframe
from labs.util.file_processing.extensions import mk_dir_abs_from_local, get_script_abs_path
from labs.util.file_processing.loader import load_from_csv, save_to_csv


def main(logs_path: str, logs_name: str):
    LOGS_PATH: str = f"{mk_dir_abs_from_local(logs_path)}/{logs_name}"
    DATAFRAME_PATH: str = f"{mk_dir_abs_from_local(DATA_OUTPUT_FOLDER)}/{LOG_CSV_FILE}"

    dataframe: pd.DataFrame
    if os.path.isfile(DATAFRAME_PATH):
        # Dataframe cache load
        dataframe = load_from_csv(DATAFRAME_PATH)
    elif os.path.isfile(LOGS_PATH):
        # Dataframe cold load
        logs: List[Dict[str, str]] = load_logs_from_file(LOGS_PATH)
        dataframe = map_tokens_to_dataframe(logs)
        save_to_csv(DATAFRAME_PATH, dataframe)
    else:
        # Data not found
        raise Exception(f"No .log files in '{logs_path}', script workdir is '{get_script_abs_path()}'")
    check_hypotheses(dataframe)
