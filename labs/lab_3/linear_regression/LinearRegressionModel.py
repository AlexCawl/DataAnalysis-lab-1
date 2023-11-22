from typing import Any, Dict

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV, RepeatedStratifiedKFold

from labs.lab_3.util.RegressionModelApi import RegressionModelApi
from labs.util.benchmarking.measuring import measure_execution_time


class LinearRegressionModel(RegressionModelApi):
    # Model state [Trained - True, otherwise - False]
    __state: bool

    # Model params for GridSearchCV (everything depends on model type API)
    __params: Dict[str, Any]

    # Model bundle from GridSearchCV (matrix of model params)
    __search: GridSearchCV

    # Cross-Validation (same for all models)
    __cv: Any = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=36851234)

    # Overall report (used to describe model state after training & testing)
    __report: Dict[str, str]

    def __init__(self):
        # init state
        self.__state = False
        # init params
        self.__params = {'fit_intercept': [True, False], 'copy_X': [True, False]}
        # init GridSearchCV based on cross-validator and params
        self.__search = GridSearchCV(estimator=LinearRegression(), param_grid=self.__params, cv=self.__cv, n_jobs=-1)
        # init logs
        self.__report = dict()

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
                "R2 score": f"{self.__search.best_score_}"
            }
        )

        # model result params
        report.update(self.__report)
        return report

    @measure_execution_time
    def train(self, *, x_train: pd.DataFrame, y_train: pd.DataFrame, path: str = "") -> None:
        # change state
        self.__state = True
        # train model
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

        # clear pyplot
        plt.clf()

        # confusion matrix plot
        plt.scatter(y_test, prediction)
        plt.savefig(f"{path}/{self.__class__.__name__}-LRM1.png")
        plt.clf()

        # regression line plot
        figure, axis = plt.subplots()
        axis.scatter(y_test, y_test - prediction)
        axis.axhline(lw=2, color='black')
        axis.set_xlabel('Observed')
        axis.set_ylabel('Residual')
        plt.savefig(f"{path}/{self.__class__.__name__}-LRM2.png")
        plt.clf()
