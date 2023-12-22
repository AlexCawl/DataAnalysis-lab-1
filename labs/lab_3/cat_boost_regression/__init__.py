from typing import Callable

from labs.lab_3.cat_boost_regression.CatBoostRegressionModel import CatBoostRegressionModel
from labs.lab_3.util.data.RegressionModelApi import RegressionModelApi

CatBoostRegressionModelFactory: Callable[[], RegressionModelApi] = lambda: CatBoostRegressionModel()
