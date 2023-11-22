from typing import List

from labs.lab_3.util.SplitDataframe import SplitDataframe


class DiscreteDataframe:
    train: List[SplitDataframe]
    test: List[SplitDataframe]

    def __init__(self, train: List[SplitDataframe], test: List[SplitDataframe]):
        self.train = train
        self.test = test
