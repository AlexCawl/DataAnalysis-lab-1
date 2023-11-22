from typing import Dict, List

import pandas as pd

from labs.lab_3.linear_regression.LinearRegressionModel import LinearRegressionModel
from labs.lab_3.util.RegressionModelApi import RegressionModelApi
from labs.lab_3.util.constants import TRAIN_FILES, TEST_FILES
from labs.lab_3.util.loader import load_atomic_dataframe
from labs.util.benchmarking.measuring import measure_execution_time
from labs.util.file_processing.configuration import DATA_OUTPUT_FOLDER
from labs.util.file_processing.extensions import mk_dir_abs_from_local


@measure_execution_time
def check_model(
        model: RegressionModelApi,
        *,
        train_dataframe: pd.DataFrame,
        train_target: pd.DataFrame,
        test_dataframe: pd.DataFrame,
        test_target: pd.DataFrame,
        log_path: str = ""
) -> None:
    model.train(x_train=train_dataframe, y_train=train_target, path=log_path)
    model.test(x_test=test_dataframe, y_test=test_target, path=log_path)
    report: Dict[str, str] = model.get_info()
    for key, value in report.items():
        print(f"{key}: {value}")


@measure_execution_time
def check_hypotheses(train_path: str, test_path: str, mode: str = "atomic"):
    log_path = mk_dir_abs_from_local(f"{DATA_OUTPUT_FOLDER}/lab3")
    # TODO place your models here
    models: List[RegressionModelApi] = [LinearRegressionModel()]

    if mode == "atomic":
        atomic_dataframe = load_atomic_dataframe(train_path, TRAIN_FILES, test_path, TEST_FILES)
        for model in models:
            check_model(
                model=model,
                train_dataframe=atomic_dataframe.train, train_target=atomic_dataframe.train_target,
                test_dataframe=atomic_dataframe.test, test_target=atomic_dataframe.test_target,
                log_path=log_path)
