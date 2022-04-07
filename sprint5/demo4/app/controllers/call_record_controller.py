from http import HTTPStatus
from flask import request, jsonify
from app.models.call_record_model import CallRecord
from app.configs.database import db
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Query
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from flask_sqlalchemy import BaseQuery
from werkzeug.exceptions import NotFound

# current_app -> db


def create_call_record():
    data = request.get_json()

    call_record = CallRecord(**data)

    session: Session = db.session()
    # Faz os atributos do objeto nao expirarem pós commit
    # session.expire_on_commit = False
    session.add(call_record)
    session.commit()

    return jsonify(call_record), HTTPStatus.CREATED


def retrive_call_by_id(call_id: int):
    # session: Session = db.session
    base_query: Query = db.session.query(CallRecord)
    # base_query: BaseQuery = db.session.query(CallRecord)

    # record = session.query(CallRecord).filter(CallRecord.id == call_id).first()
    # record = base_query.filter(CallRecord.id == call_id).first()
    # record = base_query.get(call_id)
    # record = base_query.filter_by(id=call_id).first()

    # if not record:
    #     return {"error": "id not found"}, HTTPStatus.NOT_FOUND
    # try:
    #     record = base_query.filter_by(id=call_id).one()
    # except NoResultFound:
    #     return {"error": "id not found"}, HTTPStatus.NOT_FOUND

    # try:
    #     record = base_query.filter_by(id=call_id).one_or_none()
    #     # record = base_query.filter_by(source="111111112").one_or_none()
    #     if not record:
    #         return {"error": "id not found"}, HTTPStatus.NOT_FOUND
    # except MultipleResultsFound:
    #     return {"error": "multiple results found"}

    record_query: BaseQuery = base_query.filter_by(id=call_id)
    # record = record_query.first_or_404(description="id not found")
    try:
        record = record_query.first_or_404(description="id not found")
    except NotFound as e:
        return {"error": e.description}, HTTPStatus.NOT_FOUND

    # record = record_query.get_or_404(call_id, description='id not found')

    return jsonify(record), HTTPStatus.OK
    # return
    # return jsonify(record), HTTPStatus.OK


def retrieve_call_record():
    # session: Session = db.session
    base_query: Query = db.session.query(CallRecord)

    # records = base_query.order_by(CallRecord.id).all()
    records = base_query.all()

    return jsonify(records), HTTPStatus.OK
