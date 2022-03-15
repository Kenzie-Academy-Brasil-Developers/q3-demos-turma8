from http import HTTPStatus
from flask import jsonify
from app.models.dev_model import Dev


def retrieve():
    # Retornar todos os devs do banco
    devs_list = Dev.get_all()

    devs_list = list(devs_list)
    # print(f"{devs_list[0]=}")

    # Alterar o valor da chave _id para string

    for dev in devs_list:
        # dev is dict
        dev.update({"_id": str(dev["_id"])})

        # Equivalentes
        # dev["_id"] = str(dev["_id"])

    return jsonify(devs_list), HTTPStatus.OK


# Criar um controlador para insert e delete
