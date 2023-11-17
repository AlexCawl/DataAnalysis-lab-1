import pandas as pd
from sklearn.linear_model import BayesianRidge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
import numpy as np

training_files = ['Features_Variant_1.csv', 'Features_Variant_2.csv', 'Features_Variant_3.csv',
                  'Features_Variant_4.csv', 'Features_Variant_5.csv']
test_files = ['Test_Case_1.csv', 'Test_Case_2.csv', 'Test_Case_3.csv',
              'Test_Case_4.csv', 'Test_Case_5.csv', 'Test_Case_5.csv',
              'Test_Case_6.csv', 'Test_Case_7.csv', 'Test_Case_8.csv',
              'Test_Case_9.csv', 'Test_Case_10.csv']
PATH_TRAIN = "C:/Users/denis/IdeaProjects/DataAnalysisLabs/data-in/lab_3/Training/"
PATH_TEST = "C:/Users/denis/IdeaProjects/DataAnalysisLabs/data-in/lab_3/Testing/TestSet/"


def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())


def grid_search(model, X, y):
    scores = cross_val_score(model, X, y.values.ravel(), scoring="neg_mean_squared_error", cv=10)
    rmse_scores = np.sqrt(-scores)
    display_scores(rmse_scores)


X_train_list = []
y_train_list = []

# Load training data for each variant
for i, file in enumerate(training_files):
    train_data = pd.read_csv(PATH_TRAIN + file, index_col=False, header=None)
    X_train = train_data.iloc[:, :-1]
    y_train = train_data.iloc[:, -1:]

    X_train_list.append(X_train)
    y_train_list.append(y_train)

    print(f"Variant {i + 1} - Training:")
    model = BayesianRidge()
    model.fit(X_train, y_train.values.ravel())

    # Cross-validation scores
    print("Cross-Validation:")
    grid_search(model, X_train, y_train)

# Load and test on each test case
for i, file in enumerate(test_files):
    test_data = pd.read_csv(PATH_TEST + file)
    X_test = test_data.iloc[:, :-1]
    y_test = test_data.iloc[:, -1:]

    print(f"Test Case {i + 1} - Testing:")
    y_pred = model.predict(X_test)

    # Evaluate the model
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    print("Root Mean Squared Error (RMSE):", rmse)
