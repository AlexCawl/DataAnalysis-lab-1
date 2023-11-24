from typing import List

import pandas as pd


class SplitDataframe:
    independent_variables: pd.DataFrame
    dependent_variables: pd.DataFrame

    def __init__(self, dataframe: pd.DataFrame, target_variable_names: List[str]):
        self.dependent_variables = dataframe[target_variable_names]
        self.independent_variables = dataframe.drop(columns=target_variable_names, inplace=False)
