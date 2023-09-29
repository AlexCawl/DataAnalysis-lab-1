import os
import sys


def get_script_abs_path() -> str:
    return os.path.dirname(os.path.abspath(sys.argv[0]))


def get_dir_abs_path(dir_name: str) -> str:
    return os.path.join(get_script_abs_path(), dir_name)


def mk_dir_abs_from_local(local_path: str) -> str:
    abs_path: str = get_dir_abs_path(local_path)
    if not os.path.isdir(abs_path):
        os.makedirs(abs_path)
    return abs_path
