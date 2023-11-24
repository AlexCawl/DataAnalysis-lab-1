import pandas as pd


class AtomicDataframe:
    train: pd.DataFrame
    train_target: pd.DataFrame
    test: pd.DataFrame
    test_target: pd.DataFrame

    def __init__(self, train: pd.DataFrame,
                 train_target: pd.DataFrame,
                 test: pd.DataFrame,
                 test_target: pd.DataFrame):
        self.train = train
        self.train_target = train_target
        self.test = test
        self.test_target = test_target
