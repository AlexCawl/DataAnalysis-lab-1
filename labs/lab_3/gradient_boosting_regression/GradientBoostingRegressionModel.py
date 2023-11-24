from sklearn.ensemble import GradientBoostingRegressor

from labs.lab_3.util.data.BaseRegressionModel import BaseRegressionModel


class GradientBoostingRegressionModel(BaseRegressionModel):
    def __init__(self):
        super().__init__(
            params={
                'max_depth': [6],
                'n_estimators': [3],
                'learning_rate': [1.0],
                'random_state': [42]
            },
            estimator=GradientBoostingRegressor(),
            name=f"{self.__class__.__name__}"
        )
