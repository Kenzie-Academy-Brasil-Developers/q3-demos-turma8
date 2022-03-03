from http import HTTPStatus
from flask import Flask, request, safe_join, send_file
import os

from app.video_handler.video_service import get_file_path

app = Flask(__name__)

VIDEOS_DIRECTORY = os.getenv("VIDEOS_DIRECTORY")


@app.get("/videos")
def retrieve():
    # files_list = []

    # for *_, files in os.walk("./videos"):
    #     # print(f"{root=}")
    #     # print(f"{dirs=}")
    #     print(f"{files=}")
    #     files_list.append(files)

    # Como o diretório de videos não contém subdiretorios,
    # poderiamos usar o listdir
    # files_list = os.listdir(./videos)

    # Resultados equivalentes
    # *_, files_list = list(os.walk("./videos"))[0]
    *_, files_list = next(os.walk("./videos"))

    return {"msg": files_list}, HTTPStatus.OK


@app.get("/videos/play/<filename>")
def play(filename: str):
    abs_path = os.path.abspath(VIDEOS_DIRECTORY)
    # abs_path = os.path.abspath("videos")
    # print(f"{abs_path=}")

    # filename = '../'
    filepath = safe_join(abs_path, filename)

    # TODO: Verificar se filepath é diferente de None

    return send_file(filepath), HTTPStatus.OK
    # return ""


@app.get("/videos/download/<filename>")
def download(filename: str):
    extension_format = request.args.get("format")

    if extension_format:
        filename_base = filename.split(".")[0]
        # earth.mp4 -> earth.avi (format = avi)
        converted_filename = filename_base + "." + extension_format
        # converted_filename = '.'.join([filename_base, extension_format])

        filepath = get_file_path(VIDEOS_DIRECTORY, converted_filename)
        input_path = get_file_path(VIDEOS_DIRECTORY, filename)

        command = f"ffmpeg -i {input_path} {filepath}"

        os.system(command)

        return send_file(filepath, as_attachment=True), HTTPStatus.OK

    filepath = get_file_path(VIDEOS_DIRECTORY, filename)

    return send_file(filepath, as_attachment=True), HTTPStatus.OK
