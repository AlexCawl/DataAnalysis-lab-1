from typing import Tuple, Any, List

import pandas as pd
from sklearn.feature_selection import SelectKBest, f_regression


# vanilla feature selection
def select_features(
        x_train: pd.DataFrame, y_train: pd.DataFrame,
        x_test: pd.DataFrame, k: Any = "all"
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    # configure to select a subset of features
    fs: SelectKBest = SelectKBest(score_func=f_regression, k=k)
    # learn relationship from training data
    fs.fit(x_train, y_train)
    # transform train input data
    x_train_fs = fs.transform(x_train)
    # transform test input data
    x_test_fs = fs.transform(x_test)
    return x_train_fs, x_test_fs


def select_correlated(dataframe: pd.DataFrame, target: str, k_features: int, saved_features: List[str]) -> List[str]:
    correlated_features: List[str] = list(
        dataframe.corr()[target].sort_values(ascending=False).dropna()[0:k_features].index
    )
    correlated_features.extend(saved_features)
    return correlated_features


def split_dataframe(dataframe: pd.DataFrame, *, chunk_size: int) -> List[pd.DataFrame]:
    return [dataframe[i:i + chunk_size] for i in range(0, len(dataframe), chunk_size)]
