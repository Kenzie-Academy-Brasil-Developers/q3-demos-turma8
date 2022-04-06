from http import HTTPStatus
from flask import request, jsonify
from app.models.call_record_model import CallRecord
from app.configs.database import db
from sqlalchemy.orm.session import Session

# current_app -> db


def create_call_record():
    data = request.get_json()

    call_record = CallRecord(**data)

    db.session.add(call_record)
    # print(f"{call_record=}")
    db.session.commit()

    # Outra forma de criar a sessao
    # session: Session = db.session
    # session.add(call_record)
    # session.commit()

    # print(f"{call_record.__dict__=}")
    # print(f"{call_record.id=}")
    # print(f"{call_record.__dict__=}")

    # 1 - uma forma
    call_record.__dict__.pop("_sa_instance_state")

    # 2 - segunda forma
    serialized_call_record = {
        key: value
        for key, value in call_record.__dict__.items()
        if key != "_sa_instance_state"
    }

    return jsonify(call_record.__dict__), HTTPStatus.CREATED
    # return jsonify(serialized_call_record), HTTPStatus.CREATED


def retrieve_call_record():
    return {"msg": "ROTA GET"}
