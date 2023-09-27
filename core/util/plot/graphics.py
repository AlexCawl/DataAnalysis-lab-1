from typing import Dict, List

import matplotlib.pyplot as plt
import seaborn as sns

from core.util.file_processing.extensions import mk_dir_abs_from_local


def single_plot(data: Dict[str, float], identifier: int, name: str, dir_name: str) -> None:
    plt.figure(figsize=(12, 8))
    graphic: object = sns.barplot(x=list(data.keys()), y=list(data.values()))
    graphic.set(xlabel=name, ylabel="Value")
    graphic.set_xticklabels(graphic.get_xticklabels(), rotation=90, ha="right", fontsize=10)
    plt.tight_layout()
    directory: str = mk_dir_abs_from_local(f"{dir_name}/{identifier}")
    graphic.get_figure().savefig(f"{directory}/{name.lower()}.png")
    plt.clf()


def multi_plot(data: List[float], identifier: int, name: str, dir_name: str) -> None:
    plt.figure(figsize=(12, 8))
    graphic: object = sns.histplot(data=data, kde=True)
    graphic.set(xlabel=name, ylabel="Value")
    plt.tight_layout()
    directory: str = mk_dir_abs_from_local(f"{dir_name}/{identifier}")
    graphic.get_figure().savefig(f"{directory}/{name.lower()}.png")
    plt.clf()
