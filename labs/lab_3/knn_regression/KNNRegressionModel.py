from sklearn.neighbors import KNeighborsRegressor

from labs.lab_3.util.data.BaseRegressionModel import BaseRegressionModel


class FullKNNRegressionModel(BaseRegressionModel):
    def __init__(self):
        super().__init__(
            params={
                'algorithm': ['kd_tree'],  # Keeping fixed
                'leaf_size': [15],
                'n_neighbors': [6],
                'p': [1],
                'weights': ['distance']  # Keeping fixed
            },
            estimator=KNeighborsRegressor()
        )
