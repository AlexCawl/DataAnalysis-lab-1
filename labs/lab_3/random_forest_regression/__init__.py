from typing import Callable

from labs.lab_3.random_forest_regression.RandomForestRegressionModel import RandomForestRegressionModel
from labs.lab_3.util.data.RegressionModelApi import RegressionModelApi

RandomForestRegressionModelFactory: Callable[[], RegressionModelApi] = lambda: RandomForestRegressionModel()
