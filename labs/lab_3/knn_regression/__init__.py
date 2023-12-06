from typing import Callable

from labs.lab_3.knn_regression.KNNRegressionModel import KNNRegressionModel
from labs.lab_3.util.data.RegressionModelApi import RegressionModelApi

KNNRegressionModelFactory: Callable[[], RegressionModelApi] = lambda: KNNRegressionModel()
