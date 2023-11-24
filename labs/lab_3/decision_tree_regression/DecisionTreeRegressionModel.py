from typing import Dict, Any

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.model_selection import RepeatedStratifiedKFold, GridSearchCV
from sklearn.tree import DecisionTreeRegressor

from labs.lab_3.util.data.BaseRegressionModel import BaseRegressionModel
from labs.lab_3.util.data.RegressionModelApi import RegressionModelApi


class DTRModel(BaseRegressionModel):
    # # Model state [Trained - True, otherwise - False]
    # __state: bool
    #
    # # Model params for GridSearchCV (everything depends on model type API)
    # __params: Dict[str, Any]
    #
    # # Model bundle from GridSearchCV (matrix of model params)
    # __search: GridSearchCV
    #
    # # Cross-Validation (same for all models)
    # __cv: Any = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=36851234)
    #
    # # Overall report (used to describe model state after training & testing)
    # __report: Dict[str, str]

    # def __init__(self):
    #     # init state
    #     self.__state = False
    #     # init params
    #     self.__params = {'criterion': ['friedman_mse'],
    #                      'max_depth': [10, 20],
    #                      'max_leaf_nodes': [i for i in range(65, 105, 10)],
    #                      'min_samples_split': [i for i in range(55, 105, 10)]}
    #     # init GridSearchCV based on cross-validator and params
    #     self.__search = GridSearchCV(estimator=DecisionTreeRegressor(), param_grid=self.__params, cv=self.__cv,
    #                                  scoring='r2', verbose=10, n_jobs=-1)
    #     # init logs
    #     self.__report = dict()
    #
    def __init__(self):
        # params={'criterion': ['friedman_mse', 'squared_error'],
        #                      'max_depth': [10, 20],
        #                      'max_leaf_nodes': [i for i in range(65, 106, 10)],
        #                      'min_samples_split': [i for i in range(55, 106, 10)]}

        super().__init__(
            params={'criterion': ['squared_error'],
                             'max_depth': [10, 15],
                             'max_leaf_nodes': [85, 95, 105],
                             'min_samples_split': [65, 75, 85]},
            estimator=DecisionTreeRegressor(),
            name=f"{self.__class__.__name__}",
            load_graphics=True
        )
    # def get_info(self) -> Dict[str, str]:
    #     # validation
    #     if not self.__state:
    #         raise Exception("Model not trained!")
    #
    #     # init info report
    #     report: Dict[str, str] = dict()
    #
    #     # model params
    #     report.update(
    #         {
    #             "model": "sklearn.linear_model.DecisionTreeRegressor",
    #             "best_estimator": f"{self.__search.best_estimator_}",
    #             "best_params": f"{self.__search.best_params_}",
    #             "R2 score": f"{self.__search.best_score_}"
    #         }
    #     )
    #
    #     # model result params
    #     report.update(self.__report)
    #     return report
    #
    # def train(self, x_train: pd.DataFrame, y_train: pd.DataFrame, path: str = "") -> None:
    #     # change state
    #     self.__state = True
    #     # train model
    #     self.__search.fit(X=x_train, y=y_train)
    #     print("TEST INFO")
    #     print(self.__search.best_params_)
    #     print("-"*100)
    #     print(self.__search.best_estimator_)
    #     print("-" * 100)
    #
    # def test(self, x_test: pd.DataFrame, y_test: pd.DataFrame, path: str = "") -> None:
    #     if not self.__state:
    #         raise Exception("Model not trained!")
    #
    #     prediction = self.__search.best_estimator_.predict(x_test)
    #     self.__report.update(
    #         {
    #             "mean_absolute_error": f"{metrics.mean_absolute_error(y_test, prediction)}",
    #             "mean_squared_error": f"{metrics.mean_squared_error(y_test, prediction)}",
    #             "root_mean_squared_error": f"{np.sqrt(metrics.mean_squared_error(y_test, prediction))}"
    #         }
    #     )
    #
    #     plt.scatter(y_test, prediction)
    #     plt.savefig(f"{path}/{self.__class__.__name__}-DTR1.png")
    #
    #     fig, ax = plt.subplots()
    #     ax.scatter(y_test, y_test - prediction.reshape(prediction.shape[0], 1))
    #     ax.axhline(lw=2, color='black')
    #     ax.set_xlabel('Observed')
    #     ax.set_ylabel('Residual')
    #     plt.savefig(f"{path}/{self.__class__.__name__}-DTR2.png")
