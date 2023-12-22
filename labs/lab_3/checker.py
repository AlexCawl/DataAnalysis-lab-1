from typing import List, Optional, Callable

import pandas as pd

from labs.lab_3.cat_boost_regression import CatBoostRegressionModelFactory
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
from labs.util.logger.logger import write_raw_to_log, write_json_to_log, access_log, init_log


@measure_execution_time
def check_model(
        factory: Callable[[], RegressionModelApi],
        train: pd.DataFrame, test: pd.DataFrame,
        *, output_path: Optional[str] = None, log_path: Optional[str] = None
) -> None:
    holder = RegressionSelectorHolder(train, test, TARGET_VARIABLE, SELECTED_VARIABLE, factory)
    # write model type
    write_raw_to_log(f"{holder.model_factory().__class__.__name__}", log_path=log_path)
    # train model
    holder.train(log_path=log_path)
    # test model
    holder.test(output_path=output_path)
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
    train, test = load_entire_data_and_split(train_path=train_path, test_path=test_path, fraction=0.75)

    # init models
    factories: List[Callable[[], RegressionModelApi]] = list()
    factories.append(NeuralNetworkRegressionModelFactory)
    factories.append(CatBoostRegressionModelFactory)
    factories.append(LeastSquaresLinearRegressionModelFactory)
    factories.append(RidgeLinearRegressionModelFactory)
    factories.append(RandomForestRegressionModelFactory)
    factories.append(DecisionTreeRegressionModelFactory)
    factories.append(GradientBoostingRegressionModelFactory)
    factories.append(KNNRegressionModelFactory)

    for factory in factories:
        check_model(factory, train, test, output_path=output_path, log_path=log_path)


