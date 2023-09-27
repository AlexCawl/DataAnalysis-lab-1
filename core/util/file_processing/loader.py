import pandas as pd

from core.lab_1.util.mapper import validate_dataframe
from core.util.benchmarking.measuring import measure_execution_time


@measure_execution_time
def save_to_csv(path: str, dataframe: pd.DataFrame):
    dataframe.to_csv(path, sep="\t", encoding="utf-8", index=False)


@measure_execution_time
def load_from_csv(path: str) -> pd.DataFrame:
    return validate_dataframe(pd.read_csv(path, delimiter="\t", encoding="utf-8"))
