from typing import Any, Dict, List

import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import RepeatedStratifiedKFold, GridSearchCV

from labs.lab_2.util.ClassificationModelApi import ClassificationModelApi
from labs.lab_2.util.graphics import plot_confusion_matrix, plot_points_cloud
from labs.util.benchmarking.measuring import measure_execution_time

SOLVERS: List[str] = ["svd", "eigen"]
SHRINKAGE: List[Any] = [None, 'auto', np.arange(0, 1, 0.01)]
CROSS_VALIDATOR: Any = RepeatedStratifiedKFold(n_splits=10, n_repeats=50, random_state=36851234)


class LDAModel(ClassificationModelApi):
    # Configuration params [CLASS ATTRIBUTE]
    grid: Dict[str, Any] = {
        "solver": [SOLVERS[1]],
        "shrinkage": SHRINKAGE[2]
    }
    cross_validator: Any = CROSS_VALIDATOR

    # Model params [INSTANCE ATTRIBUTE]
    __gscv: GridSearchCV
    __model: LinearDiscriminantAnalysis

    # Info params [INSTANCE ATTRIBUTE]
    __train_score: float
    __test_score: float
    __configuration_params: Any
    __matrix: Any
    __report: str | dict

    def get_info(self) -> str:
        return f"<<<   {self.__class__.__name__}   >>>\n" + \
            f"Mean Accuracy Trained: {round(self.__train_score * 100, 2)}%\n" + \
            f"Mean Accuracy Tested: {round(self.__test_score * 100, 2)}%\n" + \
            f"Configuration: {self.__configuration_params}\n" + \
            f"Confusion Matrix:\n{self.__matrix}\n" + \
            f"Classification report:\n{self.__report}"

    @measure_execution_time
    def train(self, x: pd.DataFrame, y: pd.DataFrame) -> None:
        self.__gscv = GridSearchCV(
            estimator=LinearDiscriminantAnalysis(),
            param_grid=self.grid,
            refit=True,
            scoring="accuracy",
            cv=self.cross_validator,
            n_jobs=-1
        )
        self.__gscv.fit(x, y)
        self.__model = self.__gscv.best_estimator_
        self.__train_score = self.__gscv.best_score_
        self.__configuration_params = self.__gscv.best_params_

    @measure_execution_time
    def test(self, x: pd.DataFrame, y: pd.DataFrame, path: str) -> None:
        prediction = self.__model.predict(x)
        self.__test_score = accuracy_score(y, prediction)
        self.__matrix = confusion_matrix(y, prediction)
        self.__report = classification_report(y, prediction)

        plot_confusion_matrix(self.__gscv, x, y, f"{path}/{self.__class__.__name__}-matrix.png")
        plot_points_cloud(self.__gscv, x, y, f"{path}/{self.__class__.__name__}-result.png")
