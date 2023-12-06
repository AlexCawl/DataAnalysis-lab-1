from typing import Callable

from labs.lab_3.neural_network_regression.NeuralNetworkRegresionModel import NeuralNetworkRegressionModel
from labs.lab_3.util.data.RegressionModelApi import RegressionModelApi

NeuralNetworkRegressionModelFactory: Callable[[], RegressionModelApi] = lambda: NeuralNetworkRegressionModel()
