from labs.lab_3.checker import check_hypotheses
from labs.util.benchmarking.measuring import measure_execution_time
from labs.util.file_processing.configuration import DATA_INPUT_FOLDER, TRAIN_DATASET_FOLDER, TEST_DATASET_FOLDER
from labs.util.file_processing.extensions import mk_dir_abs_from_local


@measure_execution_time
def main() -> None:
    """
    Run this only from lab3_classifications.py from content root dir.
    """
    train_path: str = f"{mk_dir_abs_from_local(DATA_INPUT_FOLDER)}/{TRAIN_DATASET_FOLDER}"
    test_path: str = f"{mk_dir_abs_from_local(DATA_INPUT_FOLDER)}/{TEST_DATASET_FOLDER}"
    check_hypotheses(train_path, test_path)
