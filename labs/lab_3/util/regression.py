from typing import Tuple, Any, List

import pandas as pd
from sklearn.feature_selection import SelectKBest, f_regression

from labs.lab_3.util.data.AtomicDataframe import AtomicDataframe


# vanilla feature selection
def select_features(x_train: pd.DataFrame, y_train: pd.DataFrame, x_test: pd.DataFrame, k: Any = "all") -> Tuple[pd.DataFrame, pd.DataFrame]:
    # configure to select a subset of features
    fs: SelectKBest = SelectKBest(score_func=f_regression, k=k)
    # learn relationship from training data
    fs.fit(x_train, y_train)
    # transform train input data
    x_train_fs = fs.transform(x_train)
    # transform test input data
    x_test_fs = fs.transform(x_test)
    return x_train_fs, x_test_fs


# atomic dataframe feature selection
def select_features_atomic(dataframe: AtomicDataframe) -> AtomicDataframe:
    x_train, x_test = select_features(dataframe.train, dataframe.train_target, dataframe.test)
    return AtomicDataframe(x_train, dataframe.train_target, x_test, dataframe.test_target)


def select_correlated(dataframe: pd.DataFrame, target: str, k_features: int, saved_features: List[str]) -> List[str]:
    correlated_features: List[str] = list(
        dataframe.corr()[target].sort_values(ascending=False).dropna()[0:k_features].index
    )
    correlated_features.extend(saved_features)
    return correlated_features
