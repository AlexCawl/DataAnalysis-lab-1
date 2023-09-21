import pandas as pd

from util.decorators import measure_execution_time
from hypotheses.website_efficiency.hypothesis_20 import clusterize


@measure_execution_time
def debug(dataframe: pd.DataFrame):
    clusterize(dataframe)


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(0, 6.28, 100)

    plt.plot(x, x ** 0.5, label='square root')
    plt.plot(x, np.sin(x), label='sinc')

    plt.xlabel('x label')
    plt.ylabel('y label')

    plt.title("test plot")

    plt.legend()
    plt.savefig("graphic.png")
