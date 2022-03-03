import os
from flask import safe_join
from datetime import datetime as dt
from werkzeug.utils import secure_filename


# from uuid import uuid4

VIDEOS_DIRECTORY = os.getenv("VIDEOS_DIRECTORY")


def get_file_path(filename: str):
    abs_path = os.path.abspath(VIDEOS_DIRECTORY)
    filepath = safe_join(abs_path, filename)

    return filepath


# file -> Objeto do tipo FileStorage
def upload_video(file):
    filename = generate_random_filename(file.filename)
    filepath = get_file_path(filename)

    file.save(filepath)


def generate_random_filename(filename: str):
    print(f"{filename}=")
    extension = filename.split(".")[-1]
    random_filename = str(dt.now().timestamp())

    # random_filename = ".".join([random_filename, extension])
    random_filename += "." + extension

    return secure_filename(random_filename)
