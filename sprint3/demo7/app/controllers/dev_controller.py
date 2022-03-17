from http import HTTPStatus
from flask import jsonify, request
from app.exceptions.dev_exc import DevIdNotFound
from app.models.dev_model import Dev


def get_devs():
    # Retornar todos os devs do banco
    devs_list = Dev.get_all()

    devs_list = list(devs_list)

    for dev in devs_list:
        Dev.serialize_dev(dev)

    return jsonify(devs_list), HTTPStatus.OK


def create_dev():
    data = request.get_json()

    try:
        dev = Dev(**data)
    except KeyError:
        return {"error": "Erro de chave"}, HTTPStatus.BAD_REQUEST

    print(f"{dev.__dict__=}")
    dev.create_dev()
    print(f"{dev.__dict__=}")

    serialized_dev = Dev.serialize_dev(dev)
    print(f"{dev.__dict__=}")

    return serialized_dev.__dict__, HTTPStatus.CREATED


def remove_dev(dev_id: str):
    deleted_dev = Dev.delete_dev(dev_id)

    if not deleted_dev:
        return {"error": f"id {dev_id} not found"}, HTTPStatus.NOT_FOUND

    Dev.serialize_dev(deleted_dev)

    return deleted_dev, HTTPStatus.OK


def get_by_gmail():
    devs = Dev.filter_by_gmail()

    serialized_devs = [Dev.serialize_dev(dev) for dev in devs]

    return jsonify(serialized_devs), HTTPStatus.OK


def update_dev(dev_id):
    data = request.get_json()

    try:
        updated_dev = Dev.update_dev(dev_id, data)
    except DevIdNotFound:
        return {"error": f"dev id {dev_id} not found."}, HTTPStatus.NOT_FOUND

    serialized_dev = Dev.serialize_dev(updated_dev)

    return serialized_dev, HTTPStatus.OK
