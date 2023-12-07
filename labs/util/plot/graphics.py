from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import seaborn as sns
from networkx import DiGraph

from labs.util.file_processing.configuration import DATA_OUTPUT_FOLDER
from labs.util.file_processing.extensions import mk_dir_abs_from_local


def single_plot(data: Dict[str, float], identifier: int, name: str, dir_name: str = DATA_OUTPUT_FOLDER) -> None:
    plt.figure(figsize=(12, 8))
    graphic: object = sns.barplot(x=list(data.keys()), y=list(data.values()))
    graphic.set(xlabel=name, ylabel="Value")
    graphic.set_xticklabels(graphic.get_xticklabels(), rotation=90, ha="right", fontsize=10)
    graphic.bar_label(graphic.containers[0], fmt="%.2f")
    plt.tight_layout()
    directory: str = mk_dir_abs_from_local(f"{dir_name}/{identifier}")
    graphic.get_figure().savefig(f"{directory}/{name.lower()}.png")
    plt.clf()


def multi_plot(data: List[float], identifier: int, name: str, dir_name: str = DATA_OUTPUT_FOLDER) -> None:
    plt.figure(figsize=(12, 8))
    graphic: object = sns.histplot(data=data, kde=False)
    graphic.set(xlabel=name, ylabel="Value")
    graphic.bar_label(graphic.containers[0], fmt="%.2f")
    plt.tight_layout()
    directory: str = mk_dir_abs_from_local(f"{dir_name}/{identifier}")
    graphic.get_figure().savefig(f"{directory}/{name.lower()}.png")
    plt.clf()


def graph_plot(nodes: List[Tuple[str, str, int]], identifier: int, name: str,
               dir_name: str = DATA_OUTPUT_FOLDER) -> None:
    graph: DiGraph = nx.DiGraph()
    graph.add_edges_from([(node[0], node[1]) for node in nodes])
    options = {
        'node_color': 'blue',
        'arrowstyle': '-|>',
    }
    nx.draw_spring(graph, with_labels=True, **options)
    directory: str = mk_dir_abs_from_local(f"{dir_name}/{identifier}")
    plt.savefig(f"{directory}/{name.lower()}.png")
    plt.clf()


def test_graphics_plot(actual: pd.DataFrame, expected: pd.DataFrame, path: str, name: str):
    # clear pyplot
    plt.clf()

    # regression plot
    plt.scatter(actual, expected)
    plt.title(f"Regression: {name}")
    plt.xlabel('Observed')
    plt.ylabel('Residual')
    plt.savefig(f"{path}/{name}-1.png")
    plt.clf()

    # regression line plot
    figure, axis = plt.subplots()
    plt.title(f"Regression error: {name}")
    axis.scatter(actual, actual - expected)
    axis.axhline(lw=1, color='black')
    axis.set_xlabel('Observed')
    axis.set_ylabel('Residual')
    plt.savefig(f"{path}/{name}-2.png")
    plt.clf()


def test_sample_regression_plot(actual: pd.DataFrame, expected: pd.DataFrame, path: str, name: str) -> None:
    # setup scatter data
    scatter_data: pd.DataFrame = pd.DataFrame()
    scatter_data['Actual'] = actual
    scatter_data['Expected'] = expected
    # setup difference data
    diff_data: pd.DataFrame = pd.DataFrame()
    diff_data['Actual'] = actual
    diff_data['Difference'] = actual - expected
    # reload painter
    plt.clf()
    sns.set(rc={'figure.figsize': (20, 8)})
    fig, axs = plt.subplots(ncols=2)
    sns.scatterplot(data=scatter_data, x='Actual', y='Expected', ax=axs[0])
    sns.regplot(data=diff_data, x='Actual', y='Difference', ax=axs[1])
    plt.savefig(f"{path}/{name}.png")
    sns.reset_orig()
    plt.clf()


def test_analytics_plot(analytics: pd.DataFrame, path: str, name: str) -> None:
    plt.clf()
    sns.set(rc={'figure.figsize': (15, 8)})
    sns.scatterplot(data=analytics, x='Actual', y='Expected', hue='hours')
    plt.savefig(f"{path}/{name}.png")
    sns.reset_orig()
    plt.clf()


def r2_score_plot(analytics: pd.DataFrame, path: str, name: str) -> None:
    ...
