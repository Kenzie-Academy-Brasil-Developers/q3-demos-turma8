import os
from flask import safe_join


def get_file_path(root_directory: str, filename: str):
    abs_path = os.path.abspath(root_directory)
    filepath = safe_join(abs_path, filename)

    return filepath
