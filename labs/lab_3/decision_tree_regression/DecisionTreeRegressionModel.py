import pandas as pd

from labs.lab_3.util.RegressionModelApi import RegressionModelApi


class DecisionTreeRegressionModel(RegressionModelApi):
    def get_info(self) -> str:
        pass

    def train(self, *, x_train: pd.DataFrame, y_train: pd.DataFrame, path: str = "") -> None:
        pass

    def test(self, *, x_test: pd.DataFrame, y_test: pd.DataFrame, path: str = "") -> None:
        pass
