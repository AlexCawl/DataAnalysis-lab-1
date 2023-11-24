from sklearn.ensemble import RandomForestRegressor

from labs.lab_3.util.data.BaseRegressionModel import BaseRegressionModel


class RFModel(BaseRegressionModel):
    def __init__(self):
        super().__init__(
            params={
                'n_estimators': [50],
                'max_depth': [15],
                'min_samples_split': [55],
                'max_leaf_nodes': [105]
            },
            estimator=RandomForestRegressor(),
            name=f"{self.__class__.__name__}",
            load_graphics=False
        )
