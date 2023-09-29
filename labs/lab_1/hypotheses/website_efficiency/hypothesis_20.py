from typing import Dict, Set, Tuple, List

import pandas as pd

from labs.lab_1.util.constants import DATA_OUTPUT_FOLDER
from labs.lab_1.util.extensions import get_users_baskets
from labs.util.benchmarking.measuring import measure_execution_time
from labs.util.plot.graphics import graph_plot


@measure_execution_time
def clusterize(dataframe: pd.DataFrame) -> List[Tuple[str, str, int]]:
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
    graph_data: List[Tuple[str, str, int]] = [(k, v[0], v[1]) for k, v in result.items()]
    graph_data = list(filter(lambda t: t[2] > 20, graph_data))
    graph_plot(graph_data, 20, "associations", DATA_OUTPUT_FOLDER)
    return graph_data
