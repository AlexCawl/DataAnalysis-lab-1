import pandas as pd

from labs.lab_2.checker import check_hypotheses
from labs.util.benchmarking.measuring import measure_execution_time


@measure_execution_time
def main():
    """
    Run this only from lab2_classifications.py from content root dir.
    """
    dataframe: pd.DataFrame
    check_hypotheses(dataframe)
