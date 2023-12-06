from typing import Callable

from labs.lab_3.gradient_boosting_regression.GradientBoostingRegressionModel import GradientBoostingRegressionModel
from labs.lab_3.util.data.RegressionModelApi import RegressionModelApi

GradientBoostingRegressionModelFactory: Callable[[], RegressionModelApi] = lambda: GradientBoostingRegressionModel()
