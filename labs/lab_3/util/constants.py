from typing import List

PATH_TRAIN: str = "data-in/lab_3/Dataset/Training"
PATH_TEST: str = "data-in/lab_3/Dataset/Testing/TestSet"

TRAIN_FILES: List[str] = [
    'Features_Variant_1.csv',
    'Features_Variant_2.csv',
    'Features_Variant_3.csv',
    'Features_Variant_4.csv',
    'Features_Variant_5.csv'
]

TEST_FILES: List[str] = ['Test_Case_1.csv', 'Test_Case_2.csv', 'Test_Case_3.csv',
                         'Test_Case_4.csv', 'Test_Case_5.csv', 'Test_Case_5.csv',
                         'Test_Case_6.csv', 'Test_Case_7.csv', 'Test_Case_8.csv',
                         'Test_Case_9.csv', 'Test_Case_10.csv']

VARIABLE_NAMES: List[str] = [
    "Page Popularity/likes", "Page Checkings", "Page talking about", "Page Category", "Derived - 5", "Derived - 6",
    "Derived - 7", "Derived - 8", "Derived - 9", "Derived - 10", "Derived - 11", "Derived - 12", "Derived - 13",
    "Derived - 14", "Derived - 15", "Derived - 16", "Derived - 17", "Derived - 18", "Derived - 19", "Derived - 20",
    "Derived - 21", "Derived - 22", "Derived - 23", "Derived - 24", "Derived - 25", "Derived - 26", "Derived - 27",
    "Derived - 28", "Derived - 29", "CC1", "CC2", "CC3", "CC4", "CC5", "Base time", "Post length", "Post Share Count",
    "Post Promotion Status", "H Local", "Post published weekday - 0", "Post published weekday - 1",
    "Post published weekday - 2", "Post published weekday - 3", "Post published weekday - 4",
    "Post published weekday - 5", "Post published weekday - 6", "Base DateTime weekday - 0",
    "Base DateTime weekday - 1", "Base DateTime weekday - 2", "Base DateTime weekday - 3", "Base DateTime weekday - 4",
    "Base DateTime weekday - 5", "Base DateTime weekday - 6", "Target Variable"
]

TARGET_VARIABLE: str = "Target Variable"
SELECTED_VARIABLE: str = "H Local"
