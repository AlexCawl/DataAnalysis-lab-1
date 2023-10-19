from typing import Any, Dict

import numpy as np
import pandas as pd
import pandas.errors
from matplotlib import pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import RepeatedStratifiedKFold, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.colors import ListedColormap
from sklearn.neighbors import RadiusNeighborsClassifier

from labs.lab_2.util.ClassificationModelApi import ClassificationModelApi
from labs.lab_2.util.constants import CLASSES


class KNNModel(ClassificationModelApi):
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
        self.__grid = {
            'n_neighbors': np.arange(1, 10, 1),
            'leaf_size': np.arange(1, 10, 1),
            'p': [1, 2],
            'weights': ['uniform', 'distance'],
            'metric': ['minkowski', 'chebyshev'],
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
        self.__search = GridSearchCV(KNeighborsClassifier(), self.__grid, scoring="accuracy",
                                     cv=self.__cv,
                                     n_jobs=-1)
        self.__results = self.__search.fit(x, y)

    def test(self, x: pd.DataFrame, y: pd.DataFrame, path: str) -> None:
        if self.__is_trained:
            prediction = self.__search.best_estimator_.predict(x)
            self.__score = accuracy_score(y, prediction)
            self.__matrix = confusion_matrix(y, prediction)
            self.__report = classification_report(y, prediction)

            # plot matrix
            plt.figure(figsize=(15, 15))
            ConfusionMatrixDisplay.from_estimator(self.__search.best_estimator_, x, y, display_labels=CLASSES)
            plt.savefig(f"{path}/{self.__class__.__name__}-matrix.png")
            plt.clf()

            # plot visualisation of method

            # h = 0.02
            # cmap_light = ListedColormap(['orange', 'cyan', 'cornflowerblue'])
            # cmap_bold = ListedColormap(['darkorange', 'c', 'darkblue'])

            # x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
            # y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
            # xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
            # mesh = self.__search.predict(np.c_[xx.ravel(), yy.ravel()])
            # mesh = mesh.reshape(xx.shape)
            # plt.figure()
            # plt.pcolormesh(xx, yy, mesh, cmap=cmap_light)
            # plt.scatter(x[:, 0], x[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=20)
            # plt.xlim(xx.min(), xx.max())
            # plt.ylim(yy.min(), yy.max())
            # plt.title("kNN classification")
            # plt.savefig(f"{path}/{self.__class__.__name__}-result.png")
            # plt.clf()



        else:
            raise Exception("Not trained already!")
