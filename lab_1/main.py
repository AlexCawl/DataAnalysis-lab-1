from typing import Tuple, List

import pandas as pd

from lab_1.hypotheses.attraction_service import hypothesis_11, hypothesis_12
from lab_1.hypotheses.user_satisfaction import hypothesis_16, hypothesis_17, hypothesis_18, hypothesis_19, hypothesis_21
from lab_1.hypotheses.website_efficiency import hypothesis_6, hypothesis_10
from util.LogDTO import LogDTO
from util.decorators import measure_execution_time
from util.loader import load_logs_from_file
from util.mapper import map_logs_to_dataframe


@measure_execution_time
def check_hypotheses(dataframe: pd.DataFrame):
    print()

    print("Вопрос №1")
    r11: Tuple[str, str] = hypothesis_11.compute_11(dataframe, 0.5)
    print(f"{r11[0]}\n{r11[1]}\n")
    r12: Tuple[str, str] = hypothesis_12.compute_12(dataframe, 20)
    print(f"{r12[0]}\n{r12[1]}\n")

    print("Вопрос №2")
    # TODO

    print("Вопрос №3")
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

    print("Вопрос №4")
    r6: Tuple[str, str] = hypothesis_6.compute_6(dataframe)
    print(f"{r6[0]}\n{r6[1]}\n")
    r10: Tuple[str, str] = hypothesis_10.compute_10(dataframe, 0.5)
    print(f"{r10[0]}\n{r10[1]}\n")


if __name__ == '__main__':
    data: Tuple[List[LogDTO], int] = load_logs_from_file("../data/access.log")
    df: pd.DataFrame = map_logs_to_dataframe(data[0], 100000)
    check_hypotheses(df)
