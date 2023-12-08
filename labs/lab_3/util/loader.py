from typing import List, Tuple, Optional

import pandas as pd

from labs.lab_3.util.constants import VARIABLE_NAMES, TRAIN_FILES, TEST_FILES
from labs.util.file_processing.loader import load_from_csv


def load_from_multiple_sources(dir_name: str, file_names: List[str]) -> List[pd.DataFrame]:
    dataframes: List[pd.DataFrame] = []
    for file_name in file_names:
        dataframe: pd.DataFrame = load_from_csv(path=f"{dir_name}/{file_name}", delimiter=',')
        dataframe.columns = VARIABLE_NAMES
        dataframes.append(dataframe)
    return dataframes


def load_from_multiple_sources_merged(dir_name: str, file_names: List[str]) -> pd.DataFrame:
    dataframes: List[pd.DataFrame] = load_from_multiple_sources(dir_name, file_names)
    return pd.concat(dataframes, ignore_index=True)


def load_entire_data_and_split(*, train_path: str, test_path: str, fraction: float, max_size: Optional[int] = None) -> Tuple[pd.DataFrame, pd.DataFrame]:
    train_base = load_from_multiple_sources_merged(train_path, TRAIN_FILES)
    test_base = load_from_multiple_sources_merged(test_path, TEST_FILES)
    all_data = pd.concat([train_base, test_base], ignore_index=True)
    all_data.drop_duplicates(inplace=True)
    all_data.drop(all_data[all_data['H Local'] == 0].index, inplace=True)
    if max_size is not None:
        all_data.drop(all_data[all_data.index > max_size].index, inplace=True)
    train = all_data.sample(frac=fraction, random_state=42)
    test = all_data.drop(train.index)
    return train, test
