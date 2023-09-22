from typing import Dict, List

import matplotlib.pyplot as plt
import seaborn as sns

from lab_1.util.decorators import measure_execution_time


@measure_execution_time
def single_plot(data: Dict[str, float], file_name: str, file_path: str) -> None:
    plt.figure(figsize=(12, 8))
    graphic: object = sns.barplot(x=list(data.keys()), y=list(data.values()))
    graphic.set(xlabel=file_name, ylabel="Value")
    graphic.set_xticklabels(graphic.get_xticklabels(), rotation=90, ha="right", fontsize=10)
    plt.tight_layout()
    graphic.get_figure().savefig(f"{file_path}/{file_name.lower()}.png")
    plt.clf()


@measure_execution_time
def multi_plot(data: List[float], file_name: str, file_path: str) -> None:
    plt.figure(figsize=(12, 8))
    graphic: object = sns.histplot(data=data, kde=True)
    graphic.set(xlabel=file_name, ylabel="Value")
    plt.tight_layout()
    graphic.get_figure().savefig(f"{file_path}/{file_name.lower()}.png")
    plt.clf()
