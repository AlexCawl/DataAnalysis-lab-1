from typing import List

from labs.lab_3.util.SplitDataframe import SplitDataframe


class DiscreteDataframe:
    train_samples: List[SplitDataframe]
    test_samples: List[SplitDataframe]

    def __init__(self, train_samples: List[SplitDataframe], test_samples: List[SplitDataframe]):
        self.train_samples = train_samples
        self.test_samples = test_samples
