from typing import Any, Optional, Dict

import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import RepeatedStratifiedKFold, cross_val_score, GridSearchCV
from sklearn.metrics import confusion_matrix

from labs.lab_2.util.ClassificationModelApi import ClassificationModelApi


class LDAModel(ClassificationModelApi):
    __is_trained: bool
    __grid: Dict[str, Any]
    __cv: RepeatedStratifiedKFold
    __search: GridSearchCV
    __results: LinearDiscriminantAnalysis

    __score: float
    __matrix: Any
    __report: str | dict

    def __init__(self) -> None:
        self.__is_trained = False
        self.__grid = {
            "solver": ["lsqr", "eigen"],
            "shrinkage": np.arange(0, 1, 0.01)
        }
        self.__cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)

    def get_info(self) -> str:
        return f"<<<   {self.__class__.__name__}   >>>\n" + \
            f"Mean Accuracy Trained: {round(self.__results.best_score_ * 100, 2)}%\n" + \
            f"Mean Accuracy Tested: {round(self.__score * 100, 2)}%\n" + \
            f"Configuration: {self.__results.best_params_}\n" + \
            f"Confusion Matrix:\n{self.__matrix}\n" + \
            f"Classification report:\n{self.__report}"

    def train(self, x: pd.DataFrame, y: pd.DataFrame) -> None:
        self.__is_trained = True
        self.__search = GridSearchCV(LinearDiscriminantAnalysis(), self.__grid, scoring="accuracy", cv=self.__cv,
                                     n_jobs=-1)
        self.__results = self.__search.fit(x, y)

    def test(self, x: pd.DataFrame, y: pd.DataFrame) -> None:
        if self.__is_trained:
            prediction = self.__search.best_estimator_.predict(x)
            self.__score = accuracy_score(y, prediction)
            self.__matrix = confusion_matrix(y, prediction)
            self.__report = classification_report(y, prediction)
        else:
            raise Exception("Not trained already!")
