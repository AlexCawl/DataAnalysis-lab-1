from sklearn.linear_model import Lasso

from labs.lab_3.linear_regression.LinearRegressionModel import LinearRegressionModel


class LassoLinearRegressionModel(LinearRegressionModel):
    def __init__(self):
        super().__init__(
            params={
                'alpha': [5.0],
                'fit_intercept': [False],
                'max_iter': [1000],
                'copy_X': [True],
                'selection': ['random']
            },
            estimator=Lasso()
        )
