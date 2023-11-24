from typing import List

import pandas as pd


class SplitDataframe:
    x: pd.DataFrame
    y: pd.DataFrame

    def __init__(self, dataframe: pd.DataFrame, target_variable_names: List[str]):
        self.y = dataframe[target_variable_names]
        self.x = dataframe.drop(columns=target_variable_names, inplace=False)
