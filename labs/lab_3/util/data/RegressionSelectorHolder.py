from typing import Dict, Optional, Callable, Iterator

import pandas as pd

from labs.lab_3.util.data.AxialDataframe import AxialDataframe
from labs.lab_3.util.data.DiscreteDataframe import DiscreteDataframe
from labs.lab_3.util.data.RegressionModelApi import RegressionModelApi


class RegressionSelectorHolder:
    target_variable: str
    selected_variable: str
    training: DiscreteDataframe
    testing: DiscreteDataframe
    discrete_solvers: Dict[int, RegressionModelApi]
    model_factory: Callable[[], RegressionModelApi]

    def __init__(
            self, train: pd.DataFrame, test: pd.DataFrame,
            target: str, selector: str,
            model_factory: Callable[[], RegressionModelApi]
    ):
        # init target variable name
        self.target_variable = target
        # init selected variable name
        self.selected_variable = selector
        # init TRAIN discrete dataframe with splitting by selector
        self.training = DiscreteDataframe(train, target, selector)
        # init TEST discrete dataframe with splitting by selector
        self.testing = DiscreteDataframe(test, target, selector)
        # init discrete solvers
        self.discrete_solvers = dict()
        # init current RegressionModelApi solver
        self.model_factory = model_factory
        # fill discrete solvers
        for key in self.training:
            self.discrete_solvers[key] = self.model_factory()

    def train(self, *, output_path: Optional[str] = None) -> None:
        for key in self.discrete_solvers:
            data: AxialDataframe = self.training[key]
            self.discrete_solvers[key].train(x_train=data.x, y_train=data.y)

    def test(self, *, output_path: Optional[str] = None) -> None:
        for key in self.discrete_solvers:
            data: AxialDataframe = self.testing[key]
            self.discrete_solvers[key].test(x_test=data.x, y_test=data.y, output_path=output_path)

    def __iter__(self) -> Iterator[int]:
        return self.discrete_solvers.__iter__()

    def __getitem__(self, item: int) -> RegressionModelApi:
        return self.discrete_solvers.__getitem__(item)
