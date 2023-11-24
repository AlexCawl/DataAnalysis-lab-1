import numpy as np
from sklearn.kernel_ridge import KernelRidge

from labs.lab_3.util.data.BaseRegressionModel import BaseRegressionModel


class KernelBasedRegressionModel(BaseRegressionModel):
    def __init__(self):
        super().__init__(
            params={"alpha": [1e0, 0.1, 1e-2, 1e-3],
                    "gamma": [0.01, 0.1, 1, 10, 100]
            },
            estimator=KernelRidge()
        )
