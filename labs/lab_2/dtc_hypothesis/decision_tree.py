from sklearn.model_selection import train_test_split, RepeatedStratifiedKFold
import pandas as pd
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.tree import DecisionTreeClassifier, plot_tree

from labs.util.benchmarking.measuring import measure_execution_time

DATA_CSV_FILE: str = f"/Users/astronely/PycharmProjects/DataAnalysisLabs/data-in/phishingData.csv"


@measure_execution_time
def decision_tree_clf():
    df = pd.read_csv(DATA_CSV_FILE)

    target_df = df['Result']
    feature_df = df.drop(columns=['Result'])

    X_train, X_test, y_train, y_test = train_test_split(feature_df,
                                                        target_df,
                                                        test_size=0.25,
                                                        random_state=2023)
    print('Размерность набора данных X_train: ', X_train.shape)
    print('Размерность набора данных Y_train: ', y_train.shape)
    print('Размерность набора данных X_test: ', X_test.shape)
    print('Размерность набора данных Y_test: ', y_test.shape)

    print('Перед применением метода кол-во меток со значением -1: {}'.format(sum(y_train == -1)))
    print('Перед применением метода кол-во меток со значением 0: {}'.format(sum(y_train == 0)))
    print('Перед применением метода кол-во меток со значением 1: {}'.format(sum(y_train == 1)))

    smote = SMOTE(random_state=2023)
    X_train, y_train = smote.fit_resample(X_train, y_train)

    print('После применением метода кол-во меток со значением -1: {}'.format(sum(y_train == -1)))
    print('После применением метода кол-во меток со значением 0: {}'.format(sum(y_train == 0)))
    print('После применением метода кол-во меток со значением 1: {}'.format(sum(y_train == 1)))

    tree_param = [{'criterion': ['entropy', 'gini'], 'max_depth': [i for i in range(1, 14)],
                   'min_samples_leaf': [i for i in range(2, 16, 2)],
                   'max_leaf_nodes': [i for i in range(2, 50, 2)]}]

    dtc_model = GridSearchCV(DecisionTreeClassifier(), tree_param, cv=12)
    dtc_model.fit(X=X_train.values, y=y_train)

    prediction = dtc_model.best_estimator_.predict(X_test)
    score = accuracy_score(y_test, prediction)
    _confusion_matrix = confusion_matrix(y_test, prediction)
    _classification_report = classification_report(y_test, prediction)

    print(f'Confusion Matrix:\n{_confusion_matrix}\n{"-"*100}\n'
          f'Classification report:\n{_classification_report}\n{"-"*100}\n')
    print(f'Лучшие найденные коэффициенты важности: {dtc_model.best_estimator_.feature_importances_}')
    print(f'Лучшие найденные параметры: {dtc_model.best_estimator_}')
    print(f'Точность на тренировочных данных: {round(dtc_model.best_score_ * 100, 2)}')
    print(f'Точность на тестовых данных: {round(score * 100, 2)}')

    features = ["SFH", "popUpWidnow", "SSLfinal_State", "Request_URL", "URL_of_Anchor", "web_traffic", "URL_Length",
                "age_of_domain", "having_IP_Address"]
    classes = ["Phishing", "Suspicious", "Not Phishing"]

    plt.figure(figsize=(15, 15))
    plot_tree(dtc_model.best_estimator_, feature_names=features, class_names=classes, filled=True)
    plt.savefig("/Users/astronely/PycharmProjects/DataAnalysisLabs/data-out/dtree.png")

    ConfusionMatrixDisplay.from_estimator(dtc_model.best_estimator_, X_test, y_test, display_labels=classes)
    plt.savefig("/Users/astronely/PycharmProjects/DataAnalysisLabs/data-out/dtree_matrix.png")


decision_tree_clf()
