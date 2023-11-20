import glob
from typing import Callable, Any, Tuple

import pandas as pd

from labs.lab_3.decision_tree_regression.DecisionTreeRegressionModel import DTRModel
from labs.util.benchmarking.measuring import measure_execution_time
from labs.util.file_processing.configuration import DATA_OUTPUT_FOLDER
from labs.util.file_processing.extensions import mk_dir_abs_from_local


@measure_execution_time
def check_model(model: Callable[[], Any], feature_df_train, target_df_train, feature_df_test, target_df_test: pd.DataFrame,
                output_path: str, balance: bool = None) -> None:

    model = model()
    model.train(feature_df_train, target_df_train)

    if balance is not None:
        model.test(feature_df_test, target_df_test, output_path, balance)
    else:
        model.test(feature_df_test, target_df_test, output_path)

    print(model.get_info())


def generate_df(train_path, test_path) -> Tuple:
    train_files = glob.glob(train_path + "/*.csv")
    test_files = glob.glob(test_path + "/*.csv")
    temp_train_dfs, temp_test_dfs = [], []

    for file in train_files:
        temp_train_dfs.append(pd.read_csv(file))

    for file in test_files:
        temp_test_dfs.append(pd.read_csv(file))

    train_df: pd.DataFrame = pd.concat(temp_train_dfs, ignore_index=True)
    test_df: pd.DataFrame = pd.concat(temp_test_dfs, ignore_index=True)

    target_df_train: pd.DataFrame = train_df['Target Variable']
    feature_df_train: pd.DataFrame = train_df.drop(columns='Target Variable')

    target_df_test: pd.DataFrame = test_df['Target Variable']
    feature_df_test: pd.DataFrame = test_df.drop(columns='Target Variable')

    return feature_df_train, target_df_train, feature_df_test, target_df_test


@measure_execution_time
def check_hypotheses(train_path: str, test_path: str):
    output_path = mk_dir_abs_from_local(f"{DATA_OUTPUT_FOLDER}/lab3")
    models = [DTRModel]
    feature_df_train, target_df_train, feature_df_test, target_df_test = generate_df(train_path, test_path)
    for model in models:
        check_model(model, feature_df_train, target_df_train, feature_df_test, target_df_test, output_path)
