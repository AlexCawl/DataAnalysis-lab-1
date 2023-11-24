import datetime
from typing import Dict, List, TextIO, Optional

import pandas as pd

from labs.lab_3.gradient_boosting_regression.GradientBoostingRegressionModel import GradientBoostingRegressionModel
from labs.lab_3.linear_regression import LINEAR_MODELS
from labs.lab_3.knn_regression.KNNRegressionModel import FullKNNRegressionModel
from labs.lab_3.neural_network_regression.NeuralNetworkRegresionModel import NeuralNetworkRegressionModel
from labs.lab_3.kb_regression.KBRegressionModel import KernelBasedRegressionModel
from labs.lab_3.util.data.AtomicDataframe import AtomicDataframe
from labs.lab_3.util.data.DiscreteDataframe import DiscreteDataframe
from labs.lab_3.util.data.RegressionModelApi import RegressionModelApi
from labs.lab_3.util.constants import TRAIN_FILES, TEST_FILES
from labs.lab_3.util.loader import load_atomic_dataframe, load_discrete_dataframe
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
        file.write(f"TIME: {datetime.datetime.now()}" + "\n")
        file.close()
    else:
        print(f"TIME: {datetime.datetime.now()}")


def write_log(
        log: Dict[str, str], title: Optional[str] = None, *,
        log_path: Optional[str] = None
) -> None:
    if log_path is not None:
        file: TextIO = open(log_path, "a")
        file.write("\n")
        if title is not None:
            file.write(title + "\n")
        for key, value in log.items():
            file.write(f"{key}: {value}" + "\n")
        file.close()
    else:
        for key, value in log.items():
            print(f"{key}: {value}")


@measure_execution_time
def atomic_check(
        model: RegressionModelApi,
        *,
        x_train: pd.DataFrame,
        y_train: pd.DataFrame,
        x_test: pd.DataFrame,
        y_test: pd.DataFrame,
        path: Optional[str] = None,
        log_path: Optional[str] = None
) -> None:
    model.train(x_train=x_train, y_train=y_train)
    model.test(x_test=x_test, y_test=y_test, path=path)
    write_log(model.get_info(), log_path=log_path)


@measure_execution_time
def discrete_check(
        model: RegressionModelApi,
        data: DiscreteDataframe,
        *,
        path: Optional[str] = None,
        log_path: Optional[str] = None
) -> None:
    # training
    for sample in data.train_samples:
        model.train(x_train=sample.x, y_train=sample.y)

    # testing
    for index, sample in enumerate(data.test_samples):
        model.test(x_test=sample.x, y_test=sample.y, path=path)
        write_log(model.get_info(), f"Iteration: {index}", log_path=log_path)

    # logging
    write_log(model.get_info(), f"Overall result", log_path=log_path)


@measure_execution_time
def check_hypotheses(train_path: str, test_path: str, *, output_path: Optional[str] = None, mode: str = "atomic"):
    log_path: Optional[str] = access_log(output_path)
    init_log(log_path)

    # TODO place your models here
    models: List[RegressionModelApi] = list()
    models.extend(LINEAR_MODELS)
    models.append(FullKNNRegressionModel())
    models.append(GradientBoostingRegressionModel())
    models.append(NeuralNetworkRegressionModel())
    models.append(KernelBasedRegressionModel())

    if mode == "atomic":
        dataframe: AtomicDataframe = load_atomic_dataframe(train_path, TRAIN_FILES, test_path, TEST_FILES)
        for model in models:
            atomic_check(
                model=model,
                x_train=dataframe.train, y_train=dataframe.train_target,
                x_test=dataframe.test, y_test=dataframe.test_target,
                path=output_path,
                log_path=log_path)
    elif mode == "discrete":
        dataframe: DiscreteDataframe = load_discrete_dataframe(train_path, TRAIN_FILES, test_path, TEST_FILES)
        for model in models:
            discrete_check(model, dataframe, path=output_path, log_path=log_path)
    else:
        raise Exception("Unknown mode!")
