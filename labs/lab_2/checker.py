from functools import reduce
from typing import Any, Callable

import pandas as pd
from sklearn.utils import resample

from labs.lab_2.dtc_hypothesis.DTModel import DTModel
from labs.lab_2.gnb_hypothesis.GNBModel import GNBModel
from labs.lab_2.knn_hypothesis.KNNModel import KNNModel
from labs.lab_2.lda_hypothesis.LDAModel import LDAModel
from labs.lab_2.svm_hypothesis.SVMModel import SVMModel
from labs.lab_2.util.constants import RESULT
from labs.lab_2.util.pandas_util import split_dataframe_into_samples
from labs.util.benchmarking.measuring import measure_execution_time
from labs.util.file_processing.configuration import DATA_OUTPUT_FOLDER
from labs.util.file_processing.extensions import mk_dir_abs_from_local


@measure_execution_time
def balance_dataframe(dataframe: pd.DataFrame) -> pd.DataFrame:
    df_classes: [pd.DataFrame] = [dataframe[dataframe['Result'] == i] for i in range(-1, 2, 1)]
    biggest_class: pd.DataFrame = reduce(lambda x, y: x if len(x) > len(y) else y, df_classes)

    balanced_data: pd.DataFrame = pd.DataFrame()
    for df_class in df_classes:
        class_resampled: pd.DataFrame = resample(df_class, replace=True, n_samples=len(biggest_class), random_state=12)
        balanced_data: pd.DataFrame = pd.concat([balanced_data, class_resampled])

    return balanced_data


@measure_execution_time
def check_model(model: Callable[[], Any], dataframe: pd.DataFrame, output_path: str, balance: bool = None) -> None:
    if balance is not None and balance:
        dataframe = balance_dataframe(dataframe)

    x_train, x_test, y_train, y_test = split_dataframe_into_samples(dataframe, RESULT)
    model = model()
    model.train_samples(x_train, y_train)

    if balance is not None:
        model.test_samples(x_test, y_test, output_path, balance)
    else:
        model.test_samples(x_test, y_test, output_path)

    print(model.get_info())


@measure_execution_time
def check_hypotheses(dataframe: pd.DataFrame):
    output_path = mk_dir_abs_from_local(f"{DATA_OUTPUT_FOLDER}/lab2")
    models = [LDAModel, SVMModel, KNNModel, GNBModel, DTModel]

    for model in models:
        if model == SVMModel:
            check_model(model, dataframe, output_path, True)
        else:
            check_model(model, dataframe, output_path)
