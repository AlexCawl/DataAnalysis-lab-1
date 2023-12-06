from typing import Dict, Iterator

import pandas as pd

from labs.lab_3.util.data.AxialDataframe import AxialDataframe


class DiscreteDataframe:
    hashMap: Dict[int, AxialDataframe]

    def __init__(self, data: pd.DataFrame, target: str, selector: str) -> None:
        """
        :param data: pandas Dataframe with required data
        :param target: target column name
        :param selector: selected column name
        """
        self.hashMap = dict()
        keys = set(list(data[selector]))
        for key in keys:
            value = data[data[selector] == key]
            self.hashMap[key] = AxialDataframe(
                x=value.drop(columns=[target, selector], inplace=False),
                y=value[target]
            )

    def __len__(self) -> int:
        return len(self.hashMap)

    def __iter__(self) -> Iterator[int]:
        return self.hashMap.__iter__()

    def __getitem__(self, item: int) -> AxialDataframe:
        return self.hashMap.__getitem__(item)
