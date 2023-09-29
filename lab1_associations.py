from labs.lab_1 import main
from labs.util.file_processing.extensions import get_script_abs_path

if __name__ == "__main__":
    # print(get_script_abs_path())
    main.main("data-in", "access.log")
