from typing import Any, Dict
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

from sklearn.model_selection import GridSearchCV, RepeatedStratifiedKFold
from sklearn import metrics

from labs.lab_3.util.RegressionModelApi import RegressionModelApi
from labs.util.benchmarking.measuring import measure_execution_time
from labs.util.plot.graphics import test_graphics_plot

class KNNRegressionModel(RegressionModelApi):
    __state: bool
    __params: Dict[str, Any]
    __search: GridSearchCV
    __cv: RepeatedStratifiedKFold
    __report: Dict[str, str]

    def __init__(self, params: Dict[str, Any], estimator: Any):
        self.__state = False
        self.__params = params
        self.__cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=36851234)
        self.__report = dict()
        self.__search = GridSearchCV(estimator=estimator, param_grid=self.__params, cv=self.__cv, n_jobs=-1)

    def get_info(self) -> Dict[str, str]:
        if not self.__state:
            raise Exception("Model not trained!")

        report: Dict[str, str] = dict()
        report.update(
            {
                "model": "sklearn.neighbors.KNeighborsRegressor",
                "best_estimator": f"{self.__search.best_estimator_}",
                "best_params": f"{self.__search.best_params_}",
                "R2 score": f"{self.__search.best_score_}"
            }
        )
        report.update(self.__report)
        return report

    @measure_execution_time
    def train(self, *, x_train: pd.DataFrame, y_train: pd.DataFrame) -> None:
        self.__state = True
        self.__search.fit(X=x_train, y=y_train)

    @measure_execution_time
    def test(self, *, x_test: pd.DataFrame, y_test: pd.DataFrame, path: str = "") -> None:
        if not self.__state:
            raise Exception("Model not trained!")

        prediction = self.__search.best_estimator_.predict(x_test)
        self.__report.update(
            {
                "mean_absolute_error": f"{metrics.mean_absolute_error(y_test, prediction)}",
                "mean_squared_error": f"{metrics.mean_squared_error(y_test, prediction)}",
                "root_mean_squared_error": f"{np.sqrt(metrics.mean_squared_error(y_test, prediction))}"
            }
        )

        test_graphics_plot(y_test, prediction, path, f"{self.__class__.__name__}-LRM")



class FullKNNRegressionModel(KNNRegressionModel):
    def __init__(self):
        super().__init__(
            params = {
                'algorithm': ['kd_tree'],  # Keeping fixed
                'leaf_size': [10,15, 18, 20],
                'n_neighbors': [6, 7],
                'p': [1],
                'weights': ['distance']  # Keeping fixed
            },
        estimator=KNeighborsRegressor()
        )