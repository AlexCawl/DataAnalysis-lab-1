from typing import List

from labs.lab_3.linear_regression.LeastSquaresModel import LeastSquaresLinearRegressionModel
from labs.lab_3.linear_regression.RidgeModel import RidgeLinearRegressionModel
from labs.lab_3.util.data.RegressionModelApi import RegressionModelApi

LINEAR_MODELS: List[RegressionModelApi] = [LeastSquaresLinearRegressionModel(), RidgeLinearRegressionModel()]
