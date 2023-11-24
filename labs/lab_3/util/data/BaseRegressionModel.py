from typing import Any, Dict, Optional

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import GridSearchCV, RepeatedStratifiedKFold

from labs.lab_3.util.data.RegressionModelApi import RegressionModelApi
from labs.util.benchmarking.measuring import measure_execution_time
from labs.util.plot.graphics import test_graphics_plot


# Base class for Linear Regression Models
# Can (and should) be reused in your models
class BaseRegressionModel(RegressionModelApi):
    # Model Name
    __name: str

    # Model state [Trained - True, otherwise - False]
    __state: bool

    # Model params for GridSearchCV (everything depends on model type API)
    __params: Dict[str, Any]

    # Model bundle from GridSearchCV (matrix of model params)
    __search: GridSearchCV

    # Cross-Validation (same for all models)
    __cv: RepeatedStratifiedKFold = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=36851234)

    # Overall report (used to describe model state after training & testing)
    __report: Dict[str, str]

    # Load graphics
    __graphics: bool

    def __init__(self, params: Dict[str, Any], estimator: Any, name: str, load_graphics: bool = False):
        # init name
        self.__name = name
        # init graphics logging
        self.__graphics = load_graphics
        # init state
        self.__state = False
        # init params
        self.__params = params
        # init cross-validator
        self.__cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=36851234)
        # init logs
        self.__report = dict()
        # init search
        self.__search = GridSearchCV(estimator=estimator, param_grid=self.__params, cv=self.__cv, n_jobs=-1)

    def get_info(self) -> Dict[str, str]:
        # validation
        if not self.__state:
            raise Exception("Model not trained!")

        # init info report
        report: Dict[str, str] = dict()

        # model params
        report.update(
            {
                "model": "sklearn.linear_model.LinearRegression",
                "best_estimator": f"{self.__search.best_estimator_}",
                "best_params": f"{self.__search.best_params_}",
            }
        )

        # model result params
        report.update(self.__report)
        return report

    @measure_execution_time
    def train(self, *, x_train: pd.DataFrame, y_train: pd.DataFrame) -> None:
        # change state
        self.__state = True
        # train model
        self.__search.fit(X=x_train, y=y_train)

    @measure_execution_time
    def test(self, *, x_test: pd.DataFrame, y_test: pd.DataFrame, path: Optional[str] = None) -> None:
        if not self.__state:
            raise Exception("Model not trained!")

        prediction = self.__search.best_estimator_.predict(x_test)
        self.__report.update(
            {
                "mean_absolute_error": f"{metrics.mean_absolute_error(y_test, prediction)}",
                "mean_squared_error": f"{metrics.mean_squared_error(y_test, prediction)}",
                "root_mean_squared_error": f"{np.sqrt(metrics.mean_squared_error(y_test, prediction))}",
                "R2 score": f"{self.__search.best_estimator_.score(x_test, y_test)}"
            }
        )

        # log graphics
        if path is not None:
            test_graphics_plot(y_test, prediction, path, f"{self.__class__.__name__}-{self.__name}")
