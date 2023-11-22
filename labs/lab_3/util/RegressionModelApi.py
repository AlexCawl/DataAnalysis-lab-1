from abc import abstractmethod
from typing import Dict

import pandas as pd


class RegressionModelApi:
    @abstractmethod
    def get_info(self) -> Dict[str, str]:
        ...

    @abstractmethod
    def train(self, *, x_train: pd.DataFrame, y_train: pd.DataFrame, path: str = "") -> None:
        ...

    @abstractmethod
    def test(self, *, x_test: pd.DataFrame, y_test: pd.DataFrame, path: str = "") -> None:
        ...
