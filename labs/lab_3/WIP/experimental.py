import os
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt
from pandas.plotting import scatter_matrix
from importlib import reload
from sklearn.feature_selection import VarianceThreshold
from collections import Counter
from sklearn.model_selection import cross_val_score

training_files: list[str] = ['Features_Variant_1.csv', 'Features_Variant_2.csv', 'Features_Variant_3.csv',
                             'Features_Variant_4.csv', 'Features_Variant_5.csv']

PATH_TRAIN: str = '../../../data-in/lab_3/Training/'
PATH_TEST: str = '../../../data-in/lab_3/Testing/TestSet/'

# Training sets
combined_train: pd.DataFrame = pd.concat(
    [pd.read_csv(PATH_TRAIN + f, index_col=False, header=None) for f in training_files], sort=False)

X_train_all = combined_train.iloc[:, :-1]
y_train_all = combined_train.iloc[:, -1:]

original_X_train_list = []
y_train_list = []

for i in range(5):
    original_X_train_list.append(pd.read_csv(PATH_TRAIN + training_files[i], index_col=False, header=None).iloc[:, :-1])
    y_train_list.append(pd.read_csv(PATH_TRAIN + training_files[i], index_col=False, header=None).iloc[:, -1:])

original_X_train_list.append(X_train_all)
y_train_list.append(y_train_all)

# Testing sets

test_files = ['Test_Case_1.csv', 'Test_Case_2.csv', 'Test_Case_3.csv',
              'Test_Case_4.csv', 'Test_Case_5.csv', 'Test_Case_5.csv',
              'Test_Case_6.csv', 'Test_Case_7.csv', 'Test_Case_8.csv',
              'Test_Case_9.csv', 'Test_Case_10.csv']

for f in test_files:
    test = pd.concat([pd.read_csv(PATH_TEST + f)])
X_test = test.iloc[:, :-1]
y_test = test.iloc[:, -1:]

X_train_list = original_X_train_list.copy()
# Grid Search (?)
# used the orinignal x training instances instead of the modifies ones
def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())


def grid_search(model):
    for i in range(6):
        scores = cross_val_score(model, original_X_train_list[i], y_train_list[i],
                                 scoring="neg_mean_squared_error", cv=10)
        rmse_scores = np.sqrt(-scores)
        if i == 5:
            print("Variant overall: ")
        else:
            print("Variant {0}: ".format(i + 1))
        display_scores(rmse_scores)


from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
for i in range(6):
    lin_reg.fit(X_train_list[i], y_train_list[i])

    rms = sqrt(mean_squared_error(y_test, lin_reg.predict(X_test)))
    if i == 5:
        print("Variant overall: ", rms)
    else:
        print("Variant {0}: ".format(i + 1), rms)
