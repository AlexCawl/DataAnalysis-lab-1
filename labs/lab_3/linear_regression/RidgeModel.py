from sklearn.linear_model import Ridge

from labs.lab_3.linear_regression.LinearRegressionModel import LinearRegressionModel


class RidgeLinearRegressionModel(LinearRegressionModel):
    def __init__(self):
        super().__init__(
            params={
                'alpha': [100.0],
                'solver': ['cholesky'],
                'copy_X': [True],
                'fit_intercept': [True]
            },
            estimator=Ridge()
        )
