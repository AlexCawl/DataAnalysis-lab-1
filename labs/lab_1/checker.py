import pandas as pd

from labs.lab_1.hypotheses.attraction_service import hypothesis_11, hypothesis_12
from labs.lab_1.hypotheses.cargo_service import hypothesis_13, hypothesis_14
from labs.lab_1.hypotheses.user_satisfaction import hypothesis_16, hypothesis_19
from labs.lab_1.hypotheses.user_satisfaction import hypothesis_21, hypothesis_17
from labs.lab_1.hypotheses.website_efficiency import hypothesis_6, hypothesis_10, hypothesis_20
from labs.util.benchmarking.measuring import measure_execution_time


@measure_execution_time
def check_hypotheses(dataframe: pd.DataFrame):
    print("Гипотеза №11")
    print(
        f"Коэффициент становление клиентом из посетителя за весь период равен: {hypothesis_11.main_11(dataframe):.2f}"
    )
    print("Гипотеза №12")
    print(
        f"Число посетителей за весь период равно: {hypothesis_12.main_12(dataframe):.2f}"
    )
    print("Гипотеза №13")
    print(
        f"Средний объем продуктовой корзины покупателя за весь период равен: {hypothesis_13.main_13(dataframe):.2f}"
    )
    print("Гипотеза №14")
    print(
        f"Товарооборот за весь период равен: {hypothesis_14.main_14(dataframe):.2f}"
    )
    print("Гипотеза №16")
    print(
        f"Среднее количество элементов в корзине клиента за весь период равно: {hypothesis_16.main_16(dataframe):.2f}"
    )
    print("Гипотеза №17")
    print(
        f"Среднее время браузинга пользователем товаров на сайте за весь период равно: {hypothesis_17.main_17(dataframe):.2f}"
    )
    print("Гипотеза №19")
    print(
        hypothesis_19.main_19(dataframe)
    )
    print("Гипотеза №21")
    print(
        f"Среднее количество переходов от одного пользователя за весь период равно: {hypothesis_21.main_21(dataframe):.2f}"
    )
    print("Гипотеза №6")
    print(
        hypothesis_6.main_6(dataframe)
    )
    print("Гипотеза №10")
    print(
        f"Последний запрос пользователя за сессию является ORDER, а не любой другой с вероятностью: {hypothesis_10.main_10(dataframe):.2f}"
    )
    print("Гипотеза №20")
    print(
        f"Граф ассоциаций сгенерирован!\n{hypothesis_20.clusterize(dataframe)}"
    )
