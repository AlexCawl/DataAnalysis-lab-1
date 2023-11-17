from typing import Callable

import pandas as pd


def merge_sources(path: str, loader: Callable[[str], pd.DataFrame]) -> pd.DataFrame:
    ...
