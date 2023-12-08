from sklearn.ensemble import HistGradientBoostingRegressor

from labs.lab_3.util.data.BaseRegressionModel import BaseRegressionModel


class GradientBoostingRegressionModel(BaseRegressionModel):
    def __init__(self):
        super().__init__(
            params={
                'max_depth': [5],
                'max_leaf_nodes': [20],
                'learning_rate': [.12]
            },
            estimator=HistGradientBoostingRegressor(),
            name=f"{self.__class__.__name__}",
            load_graphics=True
        )
