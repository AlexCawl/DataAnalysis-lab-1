import os
from typing import Tuple, List

import pandas as pd

from lab_1.hypotheses.attraction_service import hypothesis_11, hypothesis_12
from lab_1.hypotheses.cargo_service import hypothesis_13, hypothesis_14
from lab_1.hypotheses.user_satisfaction import hypothesis_16, hypothesis_17, hypothesis_21
from util.LogDTO import LogDTO
from util.decorators import measure_execution_time
from util.loader import load_logs_from_file, load_from_csv, save_to_csv
from util.mapper import map_logs_to_dataframe, prepare_dataframe


@measure_execution_time
def check_hypotheses(_dataframe: pd.DataFrame):
    print("Гипотеза №11")
    print(
        f"Коэффициент становление клиентом из посетителя за весь период равен: {hypothesis_11.main_11(_dataframe, 'data'):.2f}"
    )
    print("Гипотеза №12")
    print(
        f"Среднее число посетителей за весь период равно: {hypothesis_12.main_12(dataframe, 'data'):.2f}"
    )
    print("Гипотеза №13")
    print(
        f"Средний объем продуктовой корзины покупателя равен: {hypothesis_13.main_13(dataframe, 'data'):.2f}"
    )
    print("Гипотеза №14")
    print(
        f"Средний товарооборот за весь период равен: {hypothesis_14.main_14(dataframe, 'data'):.2f}"
    )
    print("Гипотеза №16")
    print(
        f"Среднее количество элементов в корзине клиента за весь период равно:{hypothesis_16.main_16(dataframe, 'data'):.2f}"
    )
    print("Гипотеза №17")
    print(
        f"Среднее время браузинга товаров на сайте за весь период равно:{hypothesis_17.main_17(dataframe, 'data'):.2f}"
    )
    print("Гипотеза №21")
    print(
        f"Среднее количество переходов от одного пользователя за весь период равно:{hypothesis_21.main_21(dataframe, 'data'):.2f}"
    )


LOGS_PATH: str = "data/access.log"
DATAFRAME_PATH: str = "data/logs.csv"

if __name__ == '__main__':
    dataframe: pd.DataFrame
    if os.path.isfile(DATAFRAME_PATH):
        dataframe = load_from_csv(DATAFRAME_PATH)
    elif os.path.isfile(LOGS_PATH):
        logs: Tuple[List[LogDTO], int] = load_logs_from_file(LOGS_PATH)
        dataframe = map_logs_to_dataframe(logs[0])
        save_to_csv(DATAFRAME_PATH, dataframe)
    else:
        raise Exception("No .log files in ../data")
    dataframe = prepare_dataframe(dataframe)
    check_hypotheses(dataframe)
