from typing import Tuple, List

import pandas as pd

from lab_1.hypotheses.website_efficiency import hypothesis_6
from lab_1.hypotheses.website_efficiency import hypothesis_10
from lab_1.hypotheses.user_satisfaction import hypothesis_16, hypothesis_17, hypothesis_18, hypothesis_19, hypothesis_21
from util.LogDTO import LogDTO
from util.decorators import measure_execution_time
from util.loader import load_logs_from_file
from util.mapper import map_logs_to_dataframe


@measure_execution_time
def check_hypotheses(dataframe: pd.DataFrame):
    print()
    r6: Tuple[str, str] = hypothesis_6.compute_6(dataframe)
    print(f"{r6[0]}\n{r6[1]}\n")
    r10: Tuple[str, str] = hypothesis_10.compute_10(dataframe, 0.5)
    print(f"{r10[0]}\n{r10[1]}\n")
    r16: Tuple[str, str] = hypothesis_16.compute_16(dataframe, 1)
    print(f"{r16[0]}\n{r16[1]}\n")
    r17: Tuple[str, str] = hypothesis_17.compute_17(dataframe, 20)
    print(f"{r17[0]}\n{r17[1]}\n")
    r18: Tuple[str, str] = hypothesis_18.compute_18(dataframe, 20)
    print(f"{r18[0]}\n{r18[1]}\n")
    r19: Tuple[str, str] = hypothesis_19.compute_19(dataframe)
    print(f"{r19[0]}\n{r19[1]}\n")
    r21: Tuple[str, str] = hypothesis_21.compute_21(dataframe, 4)
    print(f"{r21[0]}\n{r21[1]}\n")


if __name__ == '__main__':
    data: Tuple[List[LogDTO], int] = load_logs_from_file("../data/access.log")
    df: pd.DataFrame = map_logs_to_dataframe(data[0], 100000)
    check_hypotheses(df)
