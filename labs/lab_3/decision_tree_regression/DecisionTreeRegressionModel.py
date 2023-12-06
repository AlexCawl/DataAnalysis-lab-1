from sklearn.tree import DecisionTreeRegressor

from labs.lab_3.util.data.BaseRegressionModel import BaseRegressionModel


class DecisionTreeRegressionModel(BaseRegressionModel):
    def __init__(self):
        super().__init__(
            params={
                'criterion': ['squared_error'],
                'max_depth': [10],
                'max_leaf_nodes': [105],
                'min_samples_split': [85]
            },
            estimator=DecisionTreeRegressor(),
            name=f"{self.__class__.__name__}",
            load_graphics=True
        )
