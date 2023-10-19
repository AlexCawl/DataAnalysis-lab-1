**TODO REFACTOR!!!** \
Execution time for 'load_from_csv' took 0.0026633739471435547 seconds
Execution time for 'train' took 65.38281345367432 seconds
Execution time for 'test' took 0.5567598342895508 seconds
<<<   LDAModel   >>>
Mean Accuracy Trained: 82.0%
Mean Accuracy Tested: 82.02%
Configuration: {'shrinkage': 0.01, 'solver': 'eigen'}
Confusion Matrix:
[[192   0  14]
[ 18   2  13]
[ 28   0 139]]
Classification report:
precision    recall  f1-score   support

          -1       0.81      0.93      0.86       206
           0       1.00      0.06      0.11        33
           1       0.84      0.83      0.83       167

    accuracy                           0.82       406
macro avg       0.88      0.61      0.60       406
weighted avg       0.84      0.82      0.79       406

Execution time for 'check_model' took 65.9419527053833 seconds
Execution time for 'balance_dataframe' took 0.003285646438598633 seconds
<<<   SVMModel   >>>
Mean Accuracy Trained: 94.89%
Mean Accuracy Tested: 94.62%
Configuration: {'C': 10, 'gamma': 1, 'kernel': 'rbf'}
Confusion Matrix:
[[194   0  15]
[  3 201   0]
[ 10   6 203]]
Classification report:
precision    recall  f1-score   support

          -1       0.94      0.93      0.93       209
           0       0.97      0.99      0.98       204
           1       0.93      0.93      0.93       219

    accuracy                           0.95       632
macro avg       0.95      0.95      0.95       632
weighted avg       0.95      0.95      0.95       632

Execution time for 'check_model' took 52.89047288894653 seconds
<<<   KNNModel   >>>
Mean Accuracy Trained: 87.26%
Mean Accuracy Tested: 88.67%
Configuration: {'leaf_size': 4, 'metric': 'minkowski', 'n_neighbors': 5, 'p': 1, 'weights': 'uniform'}
Confusion Matrix:
[[190   1  15]
[  5  19   9]
[ 14   2 151]]
Classification report:
precision    recall  f1-score   support

          -1       0.91      0.92      0.92       206
           0       0.86      0.58      0.69        33
           1       0.86      0.90      0.88       167

    accuracy                           0.89       406
macro avg       0.88      0.80      0.83       406
weighted avg       0.89      0.89      0.88       406

Execution time for 'check_model' took 39.66995859146118 seconds
<<<   GNBModel   >>>
Mean Accuracy Trained: 81.35%
Mean Accuracy Tested: 81.77%
Configuration: {'priors': None, 'var_smoothing': 1e-09}
Confusion Matrix:
[[188   3  15]
[ 14   3  16]
[ 22   4 141]]
Classification report:
precision    recall  f1-score   support

          -1       0.84      0.91      0.87       206
           0       0.30      0.09      0.14        33
           1       0.82      0.84      0.83       167

    accuracy                           0.82       406
macro avg       0.65      0.62      0.62       406
weighted avg       0.79      0.82      0.80       406

Execution time for 'check_model' took 1.2941136360168457 seconds
<<<   DTModel   >>>
Mean Accuracy Trained: 87.33%
Mean Accuracy Tested: 90.39%
Configuration: {'criterion': 'entropy', 'max_depth': 6, 'max_leaf_nodes': 18, 'min_samples_leaf': 2}
Confusion Matrix:
[[187   4  15]
[  4  28   1]
[ 13   2 152]]
Classification report:
precision    recall  f1-score   support

          -1       0.92      0.91      0.91       206
           0       0.82      0.85      0.84        33
           1       0.90      0.91      0.91       167

    accuracy                           0.90       406
macro avg       0.88      0.89      0.89       406
weighted avg       0.90      0.90      0.90       406

Execution time for 'check_model' took 176.88995099067688 seconds
Execution time for 'check_hypotheses' took 336.6865346431732 seconds
Execution time for 'main' took 336.68926787376404 seconds

Process finished with exit code 0
