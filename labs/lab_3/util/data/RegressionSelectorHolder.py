from typing import Dict, Optional, Callable, Iterator

import pandas as pd
from sklearn.preprocessing import StandardScaler

from labs.lab_3.util.data.AxialDataframe import AxialDataframe
from labs.lab_3.util.data.DiscreteDataframe import DiscreteDataframe
from labs.lab_3.util.data.RegressionModelApi import RegressionModelApi
from labs.util.logger.logger import write_raw_to_log, write_json_to_log
from labs.util.plot.graphics import test_sample_regression_plot, test_analytics_plot, test_score_plot


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
        self.scaler = StandardScaler()

        for key in self.training:
            self.discrete_solvers[key] = self.model_factory()

    def train(self, *, log_path: Optional[str] = None) -> None:
        if log_path is not None:
            write_raw_to_log(f"", log_path=log_path)
        for key in self.discrete_solvers:
            data: AxialDataframe = self.training[key]

            self.scaler.fit(data.x)
            data.x = self.scaler.transform(data.x)

            self.discrete_solvers[key].train(x_train=data.x, y_train=data.y)
            if log_path is not None:
                write_raw_to_log(f"key: {key}", log_path=log_path)
                write_json_to_log(self.discrete_solvers[key].get_info(), log_path=log_path)
                write_raw_to_log(f"", log_path=log_path)

    def test(self, *, output_path: Optional[str] = None, print_all_graphics: bool = False) -> None:
        analytics: pd.DataFrame = pd.DataFrame(columns=['Actual', 'Expected', 'hours'])
        values: pd.DataFrame = pd.DataFrame(columns=['hours', 'MAE', 'MSE', 'RMSE', 'R2', 'type'], dtype=float)
        for key in self.discrete_solvers:
            data: AxialDataframe = self.testing[key]

            data.x = self.scaler.transform(data.x)

            actual, expected = self.discrete_solvers[key].test(x_test=data.x, y_test=data.y, output_path=output_path)
            # update analytics
            cur_analytics: pd.DataFrame = pd.DataFrame()
            cur_analytics['Actual'] = actual
            cur_analytics['Expected'] = expected
            cur_analytics['hours'] = key
            analytics = pd.concat([analytics, cur_analytics], axis=0)
            # update values
            cur_values = self.discrete_solvers[key].get_info()
            cur_values.update({'hours': f"{key}"})
            train_r2 = cur_values.pop('TRAIN_R2')
            test_r2 = cur_values.pop('TEST_R2')
            rowTrain = cur_values.copy()
            rowTrain.update({'R2': train_r2, 'type': 'train'})  # not sorry
            values.loc[len(values)] = pd.Series(rowTrain)
            rowTest = cur_values.copy()
            rowTest.update({'R2': test_r2, 'type': 'test'})  # not sorry
            values.loc[len(values)] = pd.Series(rowTest)
            if output_path is not None and (print_all_graphics or key == 24):
                test_sample_regression_plot(
                    actual, expected, output_path,
                    f"{self.discrete_solvers[key].__class__.__name__}-{key}h"
                )
        if output_path is not None:
            test_analytics_plot(analytics, output_path, f"{self.model_factory().__class__.__name__}")
            test_score_plot(values, output_path, f"{self.model_factory().__class__.__name__}")

    def __iter__(self) -> Iterator[int]:
        return self.discrete_solvers.__iter__()

    def __getitem__(self, item: int) -> RegressionModelApi:
        return self.discrete_solvers.__getitem__(item)
