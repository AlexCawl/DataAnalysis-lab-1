from typing import Callable

from labs.lab_3.decision_tree_regression.DecisionTreeRegressionModel import DecisionTreeRegressionModel
from labs.lab_3.util.data.RegressionModelApi import RegressionModelApi

DecisionTreeRegressionModelFactory: Callable[[], RegressionModelApi] = lambda: DecisionTreeRegressionModel()
