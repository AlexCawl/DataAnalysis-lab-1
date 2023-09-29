import os
from typing import List, Dict

import pandas as pd

from labs.lab_1.checker import check_hypotheses
from labs.lab_1.util.loader import load_logs_from_file
from labs.lab_1.util.mapper import map_tokens_to_dataframe
from labs.util.file_processing.extensions import mk_dir_abs_from_local, get_script_abs_path
from labs.util.file_processing.loader import load_from_csv, save_to_csv
from labs.util.file_processing.configuration import DATA_INPUT_FOLDER, LOG_RAW_FILE, DATA_OUTPUT_FOLDER, LOG_CSV_FILE


def main():
    """
    Run this only from lab1_associations.py from content root dir.
    """
    LOGS_PATH: str = f"{mk_dir_abs_from_local(DATA_INPUT_FOLDER)}/{LOG_RAW_FILE}"
    DATAFRAME_PATH: str = f"{mk_dir_abs_from_local(DATA_OUTPUT_FOLDER)}/{LOG_CSV_FILE}"

    dataframe: pd.DataFrame
    if os.path.isfile(DATAFRAME_PATH):
        print("Dataframe cache load")
        dataframe = load_from_csv(DATAFRAME_PATH)
    elif os.path.isfile(LOGS_PATH):
        print("Dataframe cold load")
        logs: List[Dict[str, str]] = load_logs_from_file(LOGS_PATH)
        dataframe = map_tokens_to_dataframe(logs)
        save_to_csv(DATAFRAME_PATH, dataframe)
    else:
        raise Exception(f"No .log files in '{LOGS_PATH}', script workdir is '{get_script_abs_path()}'")
    check_hypotheses(dataframe)
