import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import GridSearchCV

from labs.lab_2.util.constants import CLASSES


def plot_confusion_matrix(grid_search_cv: GridSearchCV, x: pd.DataFrame, y: pd.DataFrame, path: str) -> None:
    plt.figure(figsize=(15, 15))
    ConfusionMatrixDisplay.from_estimator(grid_search_cv.best_estimator_, x, y, display_labels=CLASSES)
    plt.savefig(path)
    plt.clf()


def plot_points_cloud(grid_search_cv: GridSearchCV, x: pd.DataFrame, y: pd.DataFrame, path: str) -> None:
    plt.figure(figsize=(15, 15))
    x_transformed = grid_search_cv.transform(x)
    colors = ['red', 'green', 'blue']
    for color, i, target_name in zip(colors, [-1, 0, 1], CLASSES):
        plt.scatter(x_transformed[y == i, 0], x_transformed[y == i, 1], alpha=.8, color=color,
                    label=target_name)
    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.savefig(path)
    plt.clf()
