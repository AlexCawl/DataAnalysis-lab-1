from sklearn.linear_model import LinearRegression

from labs.lab_3.linear_regression.LinearRegressionModel import LinearRegressionModel


class LeastSquaresLinearRegressionModel(LinearRegressionModel):
    def __init__(self):
        super().__init__(
            params={
                'fit_intercept': [False],
                'copy_X': [True]
            },
            estimator=LinearRegression()
        )
