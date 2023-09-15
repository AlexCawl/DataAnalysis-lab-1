from typing import Tuple, List

import pandas as pd

from lab_1.hypotheses.website_efficiency import hypothesis_6
from lab_1.hypotheses.website_efficiency import hypothesis_10
from util.LogDTO import LogDTO
from util.decorators import measure_execution_time
from util.loader import load_logs_from_file
from util.mapper import map_logs_to_dataframe


@measure_execution_time
def check_hypotheses(dataframe: pd.DataFrame):
    r1: Tuple[str, str] = hypothesis_6.compute_6(dataframe)
    print(f"{r1[0]}\n{r1[1]}\n")
    r2: Tuple[str, str] = hypothesis_10.compute_10(dataframe, 0.5)
    print(f"{r2[0]}\n{r2[1]}\n")


if __name__ == '__main__':
    data: Tuple[List[LogDTO], int] = load_logs_from_file("../data/access.log")
    df: pd.DataFrame = map_logs_to_dataframe(data[0], 100000)
    check_hypotheses(df)
