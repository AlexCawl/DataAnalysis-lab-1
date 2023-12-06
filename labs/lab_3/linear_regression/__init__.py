from typing import Callable

from labs.lab_3.linear_regression.LeastSquaresModel import LeastSquaresLinearRegressionModel
from labs.lab_3.linear_regression.RidgeModel import RidgeLinearRegressionModel
from labs.lab_3.util.data.RegressionModelApi import RegressionModelApi

LeastSquaresLinearRegressionModelFactory: Callable[[], RegressionModelApi] = lambda: LeastSquaresLinearRegressionModel()
RidgeLinearRegressionModelFactory: Callable[[], RegressionModelApi] = lambda: RidgeLinearRegressionModel()
