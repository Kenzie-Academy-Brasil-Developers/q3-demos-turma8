from http import HTTPStatus
from flask import request, jsonify
from app.models.call_record_model import CallRecord
from app.configs.database import db
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Query
from sqlalchemy.exc import NoResultFound, MultipleResultsFound, IntegrityError
from psycopg2.errors import UniqueViolation
from flask_sqlalchemy import BaseQuery, Pagination
from werkzeug.exceptions import NotFound
from sqlalchemy import func

# except IntegrityError as e:
# type(e.orig) == UniqueViolation

# current_app -> db


def create_call_record():
    data = request.get_json()

    call_record = CallRecord(**data)

    session: Session = db.session()
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
    session: Session = db.session
    base_query: BaseQuery = session.query(CallRecord)

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 3, type=int)

    records: Pagination = base_query.order_by(CallRecord.id).paginate(
        page=page, per_page=per_page
    )
    # records = base_query.order_by(CallRecord.id).all()
    # records = base_query.all()

    return jsonify(records.items), HTTPStatus.OK


def retrive_some_columns():
    session: Session = db.session
    base_query: Query = session.query(CallRecord.destination, CallRecord.end_time)

    records = base_query.all()
    print(f"{records[0]=}")
    print(f"{type(records[0])=}")

    # Objetos do tipo Row
    records = [record._asdict() for record in records]
    print(f"{records[0]=}")

    return jsonify(records), HTTPStatus.OK


def retrieve_group_by():
    session: Session = db.session
    """
    SELECT
        destination, COUNT(*)
    FROM call_records
    GROUP BY destination;
    """
    base_query: Query = session.query(
        CallRecord.destination.label("nova_destination"), func.count().label("contador")
    )

    records = base_query.group_by(CallRecord.destination).all()

    print(f"{records[0]=}")
    print(f"{type(records[0])=}")
    records = [record._asdict() for record in records]
    print(f"{records[0]=}")

    return jsonify(records), HTTPStatus.OK


def update_call_by_id(call_id: int):
    data = request.get_json()

    session: Session = db.session

    record = session.query(CallRecord).get(call_id)

    if not record:
        return {"error": "id not found"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        setattr(record, key, value)

    session.commit()

    # print(f"{record.chave_random=}")
    # print(f"{record.__dict__=}")
    return jsonify(record)


def delete_call_by_id(call_id: int):
    session: Session = db.session

    record = session.query(CallRecord).get(call_id)

    if not record:
        return {"error": "id not found"}, HTTPStatus.NOT_FOUND

    session.delete(record)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
    # return jsonify(record), HTTPStatus.OK
