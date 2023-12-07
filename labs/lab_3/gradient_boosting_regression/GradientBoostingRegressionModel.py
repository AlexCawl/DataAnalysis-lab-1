import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import HistGradientBoostingRegressor

from labs.lab_3.util.data.BaseRegressionModel import BaseRegressionModel


class GradientBoostingRegressionModel(BaseRegressionModel):
    def __init__(self):
        super().__init__(
            params={
                'max_depth': [5, 15, 20, 50],
                'max_leaf_nodes': [10, 20, 30, 60],
                'learning_rate': [.1, .12],
                'random_state': [4242134]
            },
            estimator=HistGradientBoostingRegressor(),
            name=f"{self.__class__.__name__}",
            load_graphics=True
        )
