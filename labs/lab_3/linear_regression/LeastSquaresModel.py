from sklearn.linear_model import LinearRegression

from labs.lab_3.linear_regression.BaseRegressionModel import BaseRegressionModel


class LeastSquaresLinearRegressionModel(BaseRegressionModel):
    def __init__(self):
        super().__init__(
            params={
                'fit_intercept': [False],
                'copy_X': [True]
            },
            estimator=LinearRegression()
        )
