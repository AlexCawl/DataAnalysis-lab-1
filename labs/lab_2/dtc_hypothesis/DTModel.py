from typing import Any, Dict

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import RepeatedStratifiedKFold, GridSearchCV

from labs.lab_2.util.ClassificationModelApi import ClassificationModelApi
from labs.lab_2.util.constants import CLASSES, FEATURES


class DTModel(ClassificationModelApi):
    __is_trained: bool
    __grid: Dict[str, Any]
    __search: GridSearchCV
    __results: LinearDiscriminantAnalysis
    __cv: RepeatedStratifiedKFold

    __score: float
    __matrix: Any
    __report: str | dict

    def __init__(self) -> None:
        self.__is_trained = False
        self.__grid = {'criterion': ['entropy', 'gini'], 'max_depth': [i for i in range(1, 10)],
                   'min_samples_leaf': [i for i in range(2, 20, 2)],
                   'max_leaf_nodes': [i for i in range(2, 20, 2)]}

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
        self.__search = GridSearchCV(DecisionTreeClassifier(), self.__grid, scoring="accuracy", refit=True, cv=self.__cv)
        self.__results = self.__search.fit(x, y)

    def test(self, x: pd.DataFrame, y: pd.DataFrame, path: str) -> None:
        if self.__is_trained:
            prediction = self.__search.best_estimator_.predict(x)
            self.__score = accuracy_score(y, prediction)
            self.__matrix = confusion_matrix(y, prediction)
            self.__report = classification_report(y, prediction)

            plt.figure(figsize=(15, 15))
            ConfusionMatrixDisplay.from_estimator(self.__search.best_estimator_, x, y, display_labels=CLASSES)
            plt.savefig(f"{path}/{self.__class__.__name__}-matrix.png")
            plt.clf()

            plt.figure(figsize=(25, 25), )
            plot_tree(self.__search.best_estimator_, feature_names=FEATURES, class_names=CLASSES, filled=True)
            plt.savefig(f"{path}/{self.__class__.__name__}-dtree.png")
            plt.clf()

        else:
            raise Exception("Not trained already!")
