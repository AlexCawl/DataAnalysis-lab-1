from sklearn.neural_network import MLPRegressor

from labs.lab_3.util.data.BaseRegressionModel import BaseRegressionModel


class NeuralNetworkRegressionModel(BaseRegressionModel):
    def __init__(self):
        super().__init__(
            params={
                'alpha': [1e-4],
                'hidden_layer_sizes': [(150, 5,)],
                'random_state': [12],
                'max_iter': [500],
                'activation': ['relu'],
                'early_stopping': [True],
                'learning_rate_init': [0.001]
            },
            estimator=MLPRegressor(),
            name=f"{self.__class__.__name__}"
        )
