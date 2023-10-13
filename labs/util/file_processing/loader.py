import pandas as pd

from labs.util.benchmarking.measuring import measure_execution_time


@measure_execution_time
def save_to_csv(path: str, dataframe: pd.DataFrame):
    dataframe.to_csv(path, sep="\t", encoding="utf-8", index=False)


@measure_execution_time
def load_from_csv(path: str, delimiter="\t") -> pd.DataFrame:
    return pd.read_csv(path, delimiter=delimiter, encoding="utf-8")
