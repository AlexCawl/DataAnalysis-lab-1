import pandas as pd

from labs.lab_2.lda_hypothesis.LDAModel import LDAModel
from labs.lab_2.util.constants import RESULT
from labs.lab_2.util.pandas_util import split_dataframe_into_samples
from labs.util.benchmarking.measuring import measure_execution_time
from labs.util.file_processing.configuration import DATA_OUTPUT_FOLDER
from labs.util.file_processing.extensions import mk_dir_abs_from_local


@measure_execution_time
def check_hypotheses(dataframe: pd.DataFrame):
    (
        X_VAL_TRAIN_SAMPLE, X_VAL_TEST_SAMPLE,
        Y_VAL_TRAIN_SAMPLE, Y_VAL_TEST_SAMPLE
    ) = split_dataframe_into_samples(dataframe, RESULT)

    output_path = mk_dir_abs_from_local(f"{DATA_OUTPUT_FOLDER}/lab2")
    lda: LDAModel = LDAModel()
    lda.train(X_VAL_TRAIN_SAMPLE, Y_VAL_TRAIN_SAMPLE)
    lda.test(X_VAL_TEST_SAMPLE, Y_VAL_TEST_SAMPLE, output_path)
    print(lda.get_info())
