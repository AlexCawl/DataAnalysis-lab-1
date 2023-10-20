# Linear Discriminant Analysis

### Code

```python
class LDAModel(ClassificationModelApi):
    # Configuration params [CLASS ATTRIBUTE]
    grid: Dict[str, Any] = {
        "solver": [SOLVERS[1]],
        "shrinkage": SHRINKAGE[2]
    }
    cross_validator: Any = CROSS_VALIDATOR

    # Model params [INSTANCE ATTRIBUTE]
    __gscv: GridSearchCV
    __model: LinearDiscriminantAnalysis

    # Info params [INSTANCE ATTRIBUTE]
    __train_score: float
    __test_score: float
    __configuration_params: Any
    __matrix: Any
    __report: str | dict

    def get_info(self) -> str:
        ...

    def train(self, x: pd.DataFrame, y: pd.DataFrame) -> None:
        self.__gscv = GridSearchCV(
            estimator=LinearDiscriminantAnalysis(),
            param_grid=self.grid,
            refit=True,
            scoring="accuracy",
            cv=self.cross_validator,
            n_jobs=-1
        )
        ...

    def test(self, x: pd.DataFrame, y: pd.DataFrame, path: str) -> None:
        ...
```

### Benchmark

- Execution time for 'train' took 65.38281345367432 seconds
- Execution time for 'test' took 0.5567598342895508 seconds
- Execution time for 'check_model' took 65.9419527053833 seconds

### Accuracy

- Mean Accuracy Trained: 82.0%

- Mean Accuracy Tested: 82.02%

### Configuration

```json
{
  "shrinkage": 0.01,
  "solver": "eigen"
}
```

### Confusion Matrix:

| Predicted:   | Phishing | Suspicious | Not phishing |
|--------------|----------|------------|--------------|
| Phishing     | 192      | 0          | 14           |
| Suspicious   | 18       | 2          | 13           |
| Not phishing | 28       | 0          | 139          |

### Classification report

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| -1           | 0.81      | 0.93   | 0.86     | 206     |
| 0            | 1.00      | 0.06   | 0.11     | 33      |
| 1            | 0.84      | 0.83   | 0.83     | 167     |
| accuracy     | -         | -      | 0.82     | 406     |
| macro avg    | 0.88      | 0.61   | 0.60     | 406     |
| weighted avg | 0.84      | 0.82   | 0.79     | 406     |

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

# Support Vector Machines

### Code

```python
class SVMModel(ClassificationModelApi):
    __is_trained: bool
    __grid: Dict[str, Any]
    __search: GridSearchCV
    __results: LinearDiscriminantAnalysis
    __cv: RepeatedStratifiedKFold

    __score: float
    __matrix: Any
    __report: str | dict

    def __init__(self) -> None:
        self.__is_trained = False
        self.__grid = {
            'C': [0.1, 1, 10, 100, 1000],
            'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
            'kernel': ['rbf']
        }
        self.__cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)

    def get_info(self) -> str:
        ...

    def train(self, x: pd.DataFrame, y: pd.DataFrame) -> None:
        self.__is_trained = True
        self.__search = GridSearchCV(
            SVC(),
            self.__grid,
            scoring="accuracy",
            refit=True,
            cv=self.__cv
        )
        self.__results = self.__search.fit(x, y)

    def test(self, x: pd.DataFrame, y: pd.DataFrame, path: str, balance: bool = False) -> None:
        if self.__is_trained:
            ...
        else:
            raise Exception("Not trained already!")

```

### Benchmarking

- Execution time for 'check_model' took 52.89047288894653 seconds

### Accuracy

- Mean Accuracy Trained: 94.89%
- Mean Accuracy Tested: 94.62%

### Configuration

```json
{
  "C": 10,
  "gamma": 1,
  "kernel": "rbf"
}
```

### Confusion Matrix

| Predicted:   | Phishing | Suspicious | Not phishing |
|--------------|----------|------------|--------------|
| Phishing     | 194      | 0          | 15           |
| Suspicious   | 3        | 201        | 0            |
| Not phishing | 10       | 6          | 203          |

### Classification report

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| -1           | 0.94      | 0.93   | 0.93     | 209     |
| 0            | 0.97      | 0.99   | 0.98     | 204     |
| 1            | 0.93      | 0.93   | 0.93     | 219     |
| accuracy     | -         | -      | 0.95     | 632     |
| macro avg    | 0.95      | 0.95   | 0.95     | 632     |
| weighted avg | 0.95      | 0.95   | 0.95     | 632     |

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

# K-Nearest Neighbors

### Code

```python
class KNNModel(ClassificationModelApi):
    __is_trained: bool
    __grid: Dict[str, Any]
    __search: GridSearchCV
    __results: KNeighborsClassifier
    __cv: RepeatedStratifiedKFold

    __score: float
    __matrix: Any
    __report: str | dict

    def __init__(self) -> None:
        self.__is_trained = False
        self.__grid = {
            'n_neighbors': np.arange(1, 10, 1),
            'leaf_size': np.arange(1, 10, 1),
            'p': [1, 2],
            'weights': ['uniform', 'distance'],
            'metric': ['minkowski', 'chebyshev'],
        }
        self.__cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)

    def get_info(self) -> str:
        ...

    def train(self, x: pd.DataFrame, y: pd.DataFrame) -> None:
        self.__is_trained = True
        self.__search = GridSearchCV(
            KNeighborsClassifier(),
            self.__grid,
            scoring="accuracy",
            cv=self.__cv,
            n_jobs=-1
        )
        self.__results = self.__search.fit(x, y)

    def test(self, x: pd.DataFrame, y: pd.DataFrame, path: str) -> None:
        if self.__is_trained:
            ...
        else:
            raise Exception("Not trained already!")

```

### Benchmarking

- Execution time for 'check_model' took 39.66995859146118 seconds

### Accuracy

- Mean Accuracy Trained: 87.26%
- Mean Accuracy Tested: 88.67%

### Configuration

```json
{
  "leaf_size": 4,
  "metric": "minkowski",
  "n_neighbors": 5,
  "p": 1,
  "weights": "uniform"
}
```

### Confusion Matrix

| Predicted:   | Phishing | Suspicious | Not phishing |
|--------------|----------|------------|--------------|
| Phishing     | 190      | 1          | 15           |
| Suspicious   | 5        | 19         | 9            |
| Not phishing | 14       | 2          | 151          |

### Classification report

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| -1           | 0.91      | 0.92   | 0.92     | 206     |
| 0            | 0.86      | 0.58   | 0.69     | 33      |
| 1            | 0.86      | 0.90   | 0.88     | 167     |
| accuracy     | -         | -      | 0.89     | 406     |
| macro avg    | 0.88      | 0.80   | 0.83     | 406     |
| weighted avg | 0.89      | 0.89   | 0.88     | 406     |

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

# Naive Bayes

### Code

```python
class GNBModel(ClassificationModelApi):
    __is_trained: bool
    __grid: Dict[str, Any]
    __search: GridSearchCV
    __results: GaussianNB
    __cv: RepeatedStratifiedKFold

    __score: float
    __matrix: Any
    __report: str | dict

    def __init__(self) -> None:
        self.__is_trained = False
        self.__grid = {
            'priors': [None],
            'var_smoothing': np.arange(0.000000001, 0.00000001, 0.000000001)
        }
        self.__cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)

    def get_info(self) -> str:
        ...

    def train(self, x: pd.DataFrame, y: pd.DataFrame) -> None:
        self.__is_trained = True
        self.__search = GridSearchCV(
            GaussianNB(),
            self.__grid,
            scoring="accuracy",
            refit=True,
            cv=self.__cv
        )
        self.__results = self.__search.fit(x, y)

    def test(self, x: pd.DataFrame, y: pd.DataFrame, path: str) -> None:
        if self.__is_trained:
            ...
        else:
            raise Exception("Not trained already!")

```

### Benchmarking

- Execution time for 'check_model' took 1.2941136360168457 seconds

### Accuracy

- Mean Accuracy Trained: 81.35%
- Mean Accuracy Tested: 81.77%

### Configuration

```json
{
  "priors": null,
  "var_smoothing": 1e-09
}
```

### Confusion Matrix

| Predicted:   | Phishing | Suspicious | Not phishing |
|--------------|----------|------------|--------------|
| Phishing     | 188      | 3          | 15           |
| Suspicious   | 14       | 3          | 16           |
| Not phishing | 22       | 4          | 141          |

### Classification report

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| -1           | 0.84      | 0.91   | 0.87     | 206     |
| 0            | 0.30      | 0.09   | 0.14     | 33      |
| 1            | 0.82      | 0.84   | 0.83     | 167     |
| accuracy     | -         | -      | 0.82     | 406     |
| macro avg    | 0.65      | 0.62   | 0.62     | 406     |
| weighted avg | 0.79      | 0.82   | 0.80     | 406     |

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

# Decision Tree Classifier

### Code

```python

class DTModel(ClassificationModelApi):
    __grid: Dict[str, Any]
    __search: GridSearchCV
    __results: LinearDiscriminantAnalysis
    __cv: RepeatedStratifiedKFold

    __score: float
    __matrix: Any
    __report: str | dict

    def __init__(self) -> None:
        self.__grid = {
            'criterion': ['entropy', 'gini'],
            'max_depth': [i for i in range(1, 10)],
            'min_samples_leaf': [i for i in range(2, 20, 2)],
            'max_leaf_nodes': [i for i in range(2, 20, 2)]
        }
        self.__cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)

    def get_info(self) -> str:
        ...

    def train(self, x: pd.DataFrame, y: pd.DataFrame) -> None:
        self.__is_trained = True
        self.__search = GridSearchCV(
            DecisionTreeClassifier(),
            self.__grid,
            scoring="accuracy",
            refit=True,
            cv=self.__cv
        )
        self.__results = self.__search.fit(x, y)

    def test(self, x: pd.DataFrame, y: pd.DataFrame, path: str) -> None:
        if self.__is_trained:
            ...
        else:
            raise Exception("Not trained already!")
```

### Benchmarking

- Execution time for 'check_model' took 176.88995099067688 seconds

### Accuracy

- Mean Accuracy Trained: 87.33%
- Mean Accuracy Tested: 90.39%

### Configuration

```json
{
  "criterion": "entropy",
  "max_depth": 6,
  "max_leaf_nodes": 18,
  "min_samples_leaf": 2
}
```

### Confusion Matrix

| Predicted:   | Phishing | Suspicious | Not phishing |
|--------------|----------|------------|--------------|
| Phishing     | 187      | 4          | 15           |
| Suspicious   | 4        | 28         | 1            |
| Not phishing | 13       | 2          | 152          |

### Classification report

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| -1           | 0.92      | 0.91   | 0.91     | 206     |
| 0            | 0.82      | 0.85   | 0.84     | 33      |
| 1            | 0.90      | 0.91   | 0.91     | 167     |
| accuracy     |           |        | 0.90     | 406     |
| macro avg    | 0.88      | 0.89   | 0.89     | 406     |
| weighted avg | 0.90      | 0.90   | 0.90     | 406     |
