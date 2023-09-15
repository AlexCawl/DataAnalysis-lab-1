import pandas as pd

from util.decorators import measure_execution_time
from hypotheses.website_efficiency.hypothesis_20 import clusterize


@measure_execution_time
def debug(dataframe: pd.DataFrame):
    clusterize(dataframe)
