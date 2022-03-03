from http import HTTPStatus
from flask import Flask, request, safe_join, send_file
import os

from app.video_package import get_file_path, upload_video

app = Flask(__name__)


@app.get("/videos")
def retrieve():
    files_list = os.listdir("./videos")

    return {"msg": files_list}, HTTPStatus.OK


@app.get("/videos/play/<filename>")
def play(filename: str):
    filepath = get_file_path(filename)

    return send_file(filepath), HTTPStatus.OK


@app.get("/videos/download/<filename>")
def download(filename: str):
    extension_format = request.args.get("format")

    # TODO: Refatorar para módulo
    if extension_format:
        filename_base = filename.split(".")[0]
        # earth.mp4 -> earth.avi (format = avi)
        converted_filename = filename_base + "." + extension_format
        # converted_filename = '.'.join([filename_base, extension_format])

        filepath = get_file_path(converted_filename)
        input_path = get_file_path(filename)

        command = f"ffmpeg -i {input_path} {filepath}"

        os.system(command)

        return send_file(filepath, as_attachment=True), HTTPStatus.OK

    filepath = get_file_path(filename)

    return send_file(filepath, as_attachment=True), HTTPStatus.OK


@app.post("/videos")
def upload():
    # <input name='video_1'>

    # ImmutableMultiDict
    files = request.files
    # request.headers
    # header = request.headers

    for file in files.values():
        upload_video(file)

    return {"msg": "videos uploaded"}, HTTPStatus.CREATED


# @app.post("/users/<user_id>/videos")
