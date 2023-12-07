import datetime
from typing import Dict, List, TextIO, Optional, Callable

import numpy as np
import pandas as pd

from labs.lab_3.decision_tree_regression import DecisionTreeRegressionModelFactory
from labs.lab_3.gradient_boosting_regression import GradientBoostingRegressionModelFactory
from labs.lab_3.knn_regression import KNNRegressionModelFactory
from labs.lab_3.linear_regression import LeastSquaresLinearRegressionModelFactory, RidgeLinearRegressionModelFactory
from labs.lab_3.neural_network_regression import NeuralNetworkRegressionModelFactory
from labs.lab_3.random_forest_regression import RandomForestRegressionModelFactory
from labs.lab_3.util.constants import TARGET_VARIABLE, SELECTED_VARIABLE
from labs.lab_3.util.data.RegressionModelApi import RegressionModelApi
from labs.lab_3.util.data.RegressionSelectorHolder import RegressionSelectorHolder
from labs.lab_3.util.loader import load_entire_data_and_split
from labs.util.benchmarking.measuring import measure_execution_time


def access_log(path: Optional[str]) -> Optional[str]:
    log_file: str = "lab3.log"
    if path is not None:
        return f"{path}/{log_file}"
    else:
        return None


def init_log(log_path: Optional[str] = None):
    if log_path is not None:
        file: TextIO = open(log_path, "w")
        file.write(f"TIME: {datetime.datetime.now()}" + "\n\n")
        file.close()
    else:
        print(f"TIME: {datetime.datetime.now()}")


def write_json_to_log(
        log: Dict[str, str],
        *, log_path: Optional[str] = None
) -> None:
    if log_path is not None:
        file: TextIO = open(log_path, "a")
        for key, value in log.items():
            file.write(f"{key}: {value}" + "\n")
        file.close()
    else:
        for key, value in log.items():
            print(f"{key}: {value}")


def write_raw_to_log(
        log: str,
        *, log_path: Optional[str] = None
) -> None:
    if log_path is not None:
        file: TextIO = open(log_path, "a")
        file.write(f"{log}" + "\n")
        file.close()
    else:
        print(f"{log}")


@measure_execution_time
def check_model(
        factory: Callable[[], RegressionModelApi],
        train: pd.DataFrame, test: pd.DataFrame,
        *, output_path: Optional[str] = None, log_path: Optional[str] = None
) -> None:
    holder = RegressionSelectorHolder(train, test, TARGET_VARIABLE, SELECTED_VARIABLE, factory)
    holder.train(output_path=output_path)
    holder.test(output_path=output_path)
    # write model type
    write_raw_to_log(f"{holder.model_factory().__class__.__name__}", log_path=log_path)
    # write general info about entire model
    common: Dict[str, str] = {
        "MAE": f"{np.median(list(map(lambda x: float(x), [holder[model_key].get_info()['MAE'] for model_key in holder])))}",
        "MSE": f"{np.median(list(map(lambda x: float(x), [holder[model_key].get_info()['MSE'] for model_key in holder])))}",
        "RMSE": f"{np.median(list(map(lambda x: float(x), [holder[model_key].get_info()['RMSE'] for model_key in holder])))}",
        "R2": f"{np.median(list(map(lambda x: float(x), [holder[model_key].get_info()['R2'] for model_key in holder])))}"
    }
    write_json_to_log(common, log_path=log_path)
    write_raw_to_log(f"", log_path=log_path)
    # write each selected model info
    for model_key in holder:
        write_raw_to_log(f"key: {model_key}", log_path=log_path)
        write_json_to_log(holder[model_key].get_info(), log_path=log_path)
        write_raw_to_log(f"", log_path=log_path)


@measure_execution_time
def check_hypotheses(train_path: str, test_path: str, *, output_path: Optional[str] = None):
    # init logger
    log_path: Optional[str] = access_log(output_path)
    init_log(log_path)

    # init data
    train, test = load_entire_data_and_split(train_path=train_path, test_path=test_path, fraction=0.75, max_size=200000)

    # init models
    factories: List[Callable[[], RegressionModelApi]] = list()
    # factories.append(LeastSquaresLinearRegressionModelFactory)
    # factories.append(RidgeLinearRegressionModelFactory)
    # factories.append(NeuralNetworkRegressionModelFactory)
    # factories.append(RandomForestRegressionModelFactory)
    # factories.append(DecisionTreeRegressionModelFactory)
    factories.append(GradientBoostingRegressionModelFactory)
    # factories.append(KNNRegressionModelFactory)

    for factory in factories:
        check_model(factory, train, test, output_path=output_path, log_path=log_path)
