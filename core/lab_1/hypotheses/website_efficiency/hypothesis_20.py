from typing import Dict, Set, Tuple

import pandas as pd

from core.lab_1.util.extensions import get_users_baskets
from core.util.benchmarking.measuring import measure_execution_time


@measure_execution_time
def clusterize(dataframe: pd.DataFrame) -> Dict[str, Tuple[str, int]]:
    users_baskets: Dict[str, Set[str]] = get_users_baskets(dataframe)
    cluster: Dict[str, Dict[str, int]] = dict()
    result: Dict[str, Tuple[str, int]] = dict()

    def update(_item_id: str, _common_items: Set[str]) -> None:
        if _item_id not in cluster:
            cluster.update({_item_id: dict()})

        subcluster: Dict[str, int] = cluster[_item_id]
        for _common_item in _common_items:
            if _common_item != _item_id:
                subcluster.update({_common_item: subcluster.get(_common_item, 0) + 1})

    for basket in users_baskets.values():
        for item in basket:
            update(item, basket)

    for key, value in cluster.items():
        subitem: Tuple[str, int] = max(value.items(), key=lambda k: k[1])
        result.update({key: subitem})
    return result
