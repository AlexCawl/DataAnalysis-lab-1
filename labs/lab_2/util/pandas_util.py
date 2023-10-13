from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split


def split_dataframe_into_samples(dataframe: pd.DataFrame, result_column_name: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    params: pd.DataFrame = dataframe.drop(columns=[result_column_name])
    result_values: pd.DataFrame = dataframe[result_column_name]
    return train_test_split(params,
                            result_values,
                            test_size=0.30,
                            random_state=12)
