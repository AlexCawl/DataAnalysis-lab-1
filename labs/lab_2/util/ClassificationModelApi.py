from abc import ABC, abstractmethod
from typing import Any

import pandas as pd


class ClassificationModelApi(ABC):
    @abstractmethod
    def get_info(self) -> str:
        ...

    @abstractmethod
    def train(self, x_train_val: pd.DataFrame, y_train_val: pd.DataFrame) -> None:
        ...

    @abstractmethod
    def test(self, x_test_val: pd.DataFrame, y_test_val: pd.DataFrame, path: str) -> None:
        ...
