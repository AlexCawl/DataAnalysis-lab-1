from typing import List

import pandas as pd

from labs.lab_3.util.AtomicDataframe import AtomicDataframe
from labs.lab_3.util.DiscreteDataframe import DiscreteDataframe
from labs.lab_3.util.SplitDataframe import SplitDataframe
from labs.lab_3.util.constants import VARIABLE_NAMES
from labs.util.file_processing.loader import load_from_csv


def load_atomic_dataframe(
        path_train_dataframes: str,
        train_dataframes_names: List[str],
        path_test_dataframes: str,
        test_dataframes_names: List[str]
) -> AtomicDataframe:
    def load(path: str, names: List[str]) -> List[pd.DataFrame]:
        dataframes: List[pd.DataFrame] = []
        for name in names:
            dataframe: pd.DataFrame = load_from_csv(path=f"{path}/{name}", delimiter=',')
            dataframe.columns = VARIABLE_NAMES
            dataframes.append(dataframe)
        return dataframes

    # loading raw dataframes
    train_dataframes: List[pd.DataFrame] = load(path_train_dataframes, train_dataframes_names)
    test_dataframes: List[pd.DataFrame] = load(path_test_dataframes, test_dataframes_names)

    # concatenating dataframes
    train_atomic_dataframe: pd.DataFrame = pd.concat(train_dataframes, ignore_index=True)
    train_atomic_dataframe.drop_duplicates(inplace=True)
    test_atomic_dataframe: pd.DataFrame = pd.concat(test_dataframes, ignore_index=True)

    return AtomicDataframe(
        train=train_atomic_dataframe.drop(columns=["Target Variable"], inplace=False),
        train_target=train_atomic_dataframe[["Target Variable"]],
        test=test_atomic_dataframe.drop(columns=["Target Variable"], inplace=False),
        test_target=test_atomic_dataframe[["Target Variable"]]
    )


def load_discrete_dataframe(
        path_train_dataframes: str,
        train_dataframes_names: List[str],
        path_test_dataframes: str,
        test_dataframes_names: List[str]
) -> DiscreteDataframe:
    def load(path: str, names: List[str], target: List[str]) -> List[SplitDataframe]:
        raw_dataframes: List[pd.DataFrame] = []
        for name in names:
            dataframe: pd.DataFrame = load_from_csv(path=f"{path}/{name}", delimiter=',')
            dataframe.columns = VARIABLE_NAMES
            raw_dataframes.append(dataframe)
        return [SplitDataframe(df, target) for df in raw_dataframes]

    train_dataframes: List[SplitDataframe] = load(path_train_dataframes, train_dataframes_names, ["Target Variable"])
    test_dataframes: List[SplitDataframe] = load(path_test_dataframes, test_dataframes_names, ["Target Variable"])
    return DiscreteDataframe(train=train_dataframes, test=test_dataframes)
