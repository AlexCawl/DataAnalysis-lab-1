from typing import List

import pandas as pd


class AxialDataframe:
    """
    A class that encapsulates commonly used divisions of a source dataframe into independent and dependent variables.

    x - independent variables in dataframe

    y - dependent on X values variables in dataframe
    """
    x: pd.DataFrame
    y: pd.DataFrame

    def __init__(self, x: pd.DataFrame, y: pd.DataFrame) -> None:
        self.y = y
        self.x = x

    @classmethod
    def from_single_target(cls, data: pd.DataFrame, target: str):
        Y: pd.DataFrame = data[target]
        X: pd.DataFrame = data.drop(columns=[target], inplace=False)
        return AxialDataframe(X, Y)

    @classmethod
    def from_multiple_targets(cls, data: pd.DataFrame, targets: List[str]):
        Y: pd.DataFrame = data[targets]
        X: pd.DataFrame = data.drop(columns=targets, inplace=False)
        return AxialDataframe(X, Y)

    def __len__(self):
        return min(len(self.x), len(self.y))
