from typing import Tuple, List, Dict

import pandas as pd
import os

from lab_1.hypotheses.attraction_service import hypothesis_11, hypothesis_12
from lab_1.hypotheses.cargo_service import hypothesis_13, hypothesis_14
from lab_1.hypotheses.user_satisfaction import hypothesis_16, hypothesis_17, hypothesis_19, hypothesis_21
from lab_1.hypotheses.website_efficiency import hypothesis_6, hypothesis_10, hypothesis_20
from util.LogDTO import LogDTO
from util.decorators import measure_execution_time
from util.loader import load_logs_from_file, load_from_csv, save_to_csv
from util.mapper import map_logs_to_dataframe


@measure_execution_time
def check_hypotheses(dataframe: pd.DataFrame):
    print()

    print("Вопрос №1")
    r11: Tuple[float, str] = hypothesis_11.compute_11(dataframe)
    print(f"{r11[0]}\n{r11[1]}\n")
    r12: Tuple[float, str] = hypothesis_12.compute_12(dataframe)
    print(f"{r12[0]}\n{r12[1]}\n")

    print("Вопрос №2")
    r13: Tuple[float, str] = hypothesis_13.compute_13(dataframe)
    print(f"{r13[0]}\n{r13[1]}\n")
    r14: Tuple[float, str] = hypothesis_14.compute_14(dataframe)
    print(f"{r14[0]}\n{r14[1]}\n")

    print("Вопрос №3")
    r16: Tuple[float, str] = hypothesis_16.compute_16(dataframe)
    print(f"{r16[0]}\n{r16[1]}\n")
    r17: Tuple[float, str] = hypothesis_17.compute_17(dataframe)
    print(f"{r17[0]}\n{r17[1]}\n")
    r19: Tuple[str, str] = hypothesis_19.compute_19(dataframe)
    print(f"{r19[0]}\n{r19[1]}\n")
    r21: Tuple[float, str] = hypothesis_21.compute_21(dataframe)
    print(f"{r21[0]}\n{r21[1]}\n")

    print("Вопрос №4")
    r6: Tuple[str, str] = hypothesis_6.compute_6(dataframe)
    print(f"{r6[0]}\n{r6[1]}\n")
    r10: Tuple[float, str] = hypothesis_10.compute_10(dataframe)
    print(f"{r10[0]}\n{r10[1]}\n")
    r20: Dict[str, Tuple[str, int]] = hypothesis_20.clusterize(dataframe)
    print("Ассоциативные товары:")
    for key, value in r20.items():
        print(f"{key} -> {value[0]} [{value[1]}]")


LOGS_PATH: str = "../data/access.log"
DATAFRAME_PATH: str = "../data/logs.csv"

if __name__ == '__main__':
    df: pd.DataFrame
    if os.path.isfile(DATAFRAME_PATH):
        df = load_from_csv(DATAFRAME_PATH)
    elif os.path.isfile(LOGS_PATH):
        data: Tuple[List[LogDTO], int] = load_logs_from_file(LOGS_PATH)
        df = map_logs_to_dataframe(data[0])
        save_to_csv(DATAFRAME_PATH, df)
    else:
        raise Exception("No .log files in ../data")
    check_hypotheses(df)
