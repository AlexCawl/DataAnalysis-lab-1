import pandas as pd

from labs.lab_2.lda_hypothesis.LDAModel import LDAModel
from labs.lab_2.util.constants import RESULT
from labs.lab_2.util.pandas_util import split_dataframe_into_samples
from labs.util.benchmarking.measuring import measure_execution_time


@measure_execution_time
def check_hypotheses(dataframe: pd.DataFrame):
    (
        X_VAL_TRAIN_SAMPLE, X_VAL_TEST_SAMPLE,
        Y_VAL_TRAIN_SAMPLE, Y_VAL_TEST_SAMPLE
    ) = split_dataframe_into_samples(dataframe, RESULT)

    lda: LDAModel = LDAModel()
    lda.train(X_VAL_TRAIN_SAMPLE, Y_VAL_TRAIN_SAMPLE)
    lda.test(X_VAL_TEST_SAMPLE, Y_VAL_TEST_SAMPLE)
    print(lda.get_info())
