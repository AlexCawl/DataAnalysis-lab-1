from typing import Dict, Any

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.model_selection import RepeatedStratifiedKFold, GridSearchCV
from sklearn.tree import DecisionTreeRegressor

from labs.lab_3.util.RegressionModelApi import RegressionModelApi


class DTRModel(RegressionModelApi):
    __is_trained: bool
    __grid: Dict[str, Any]
    __search: GridSearchCV
    __cv: RepeatedStratifiedKFold
    # __results = None
    __report: str | dict

    def __init__(self):
        self.__results = None
        self._RMSE = None
        self._MSE = None
        self._MAE = None
        self.__is_trained = False
        self.__grid = {'criterion': ['friedman_mse'],
                       'max_depth': [i for i in range(5, 20, 2)],
                       'max_leaf_nodes': [i for i in range(20, 60, 10)],
                       'min_samples_split': [i for i in range(20, 80, 10)]}
        # self.__grid = {'criterion': ['friedman_mse'],
        #                'max_depth': [10],
        #                'max_leaf_nodes': [40],
        #                'min_samples_split': [70]}

        self.__cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)

    def get_info(self) -> str:
        return f"<<<   {self.__class__.__name__}   >>>\n" + \
            f"R-Squared trained: {round(self.__results.best_score_ * 100, 2)}%\n" + \
            f"MAE Tested: {self._MAE}%\n" + \
            f"MSE Tested: {self._MSE}%\n" + \
            f"RMSE Tested: {self._RMSE}%\n" + \
            f"Configuration: {self.__results.best_params_}\n"

    def train(self, x_train: pd.DataFrame, y_train: pd.DataFrame) -> None:
        self.__is_trained = True
        self.__search = GridSearchCV(DecisionTreeRegressor(), self.__grid, cv=6)
        self.__results = self.__search.fit(X=x_train, y=y_train)

    def test(self, x_test: pd.DataFrame, y_test: pd.DataFrame, path: str = "") -> None:
        if self.__is_trained:
            prediction = self.__search.best_estimator_.predict(x_test)
            self._MAE = metrics.mean_absolute_error(y_test, prediction)
            self._MSE = metrics.mean_absolute_error(y_test, prediction)
            self._RMSE = np.sqrt(self._MSE)

            plt.scatter(y_test, prediction)
            plt.savefig(f"{path}/{self.__class__.__name__}-DTR1.png")

            fig, ax = plt.subplots()
            ax.scatter(y_test, y_test - prediction)
            ax.axhline(lw=2, color='black')
            ax.set_xlabel('Observed')
            ax.set_ylabel('Residual')
            plt.savefig(f"{path}/{self.__class__.__name__}-DTR2.png")

        else:
            raise Exception("Not trained already!")
