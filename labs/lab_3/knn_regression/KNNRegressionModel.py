from sklearn.neighbors import KNeighborsRegressor

from labs.lab_3.util.data.BaseRegressionModel import BaseRegressionModel


class KNNRegressionModel(BaseRegressionModel):
    def __init__(self):
        super().__init__(
            params={
                'algorithm': ['kd_tree'],  # Keeping fixed
                'leaf_size': [15],
                'n_neighbors': [6],
                'p': [1],
                'weights': ['distance']  # Keeping fixed
            },
            estimator=KNeighborsRegressor(),
            name=f"{self.__class__.__name__}",
            load_graphics=True
        )
