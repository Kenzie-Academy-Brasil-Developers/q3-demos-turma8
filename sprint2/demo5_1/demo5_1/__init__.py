from flask import Flask, jsonify, request
from datetime import datetime as dt
from http import HTTPStatus
from copy import deepcopy

from demo5_1.csv_package.csv_module import (
    read_events_from_csv,
    rewrite_events_in_csv,
    write_event_in_csv,
)

from .events_package.event_service import is_in_interval, serialize_event, validate_keys

app = Flask(__name__)


@app.get("/h")
def home():
    events = read_events_from_csv()
    return jsonify(events), 200


@app.get("/h/1703")
def retrive_1702():
    events = read_events_from_csv()
    events_found = [
        event for event in events if dt.fromtimestamp(event["timestamp"]).year == 1702
    ]

    count = len(events_found)

    return {"count": count, "events": events_found}, HTTPStatus.OK


@app.get("/h/year/<int:year>")
def retrive_by_year(year):
    events = read_events_from_csv()

    events_found = [
        event for event in events if dt.fromtimestamp(event["timestamp"]).year == year
    ]

    count = len(events_found)

    return {"count": count, "events": events_found}, HTTPStatus.OK


@app.get("/h/day/<int:day>")
def retrive_by_day(day):
    events = read_events_from_csv()

    events_found = [
        event for event in events if dt.fromtimestamp(event["timestamp"]).day == day
    ]

    count = len(events_found)

    return {"count": count, "events": events_found}, HTTPStatus.OK


@app.get("/h/query")
def retrieve_by_date_interval():
    events = read_events_from_csv()

    begin_date = request.args.get("begin_date")
    end_date = request.args.get("end_date")

    if not begin_date or not end_date:
        return {"error": "you must pass a begin and end date"}, HTTPStatus.BAD_REQUEST

    events_found = [
        serialize_event(event)
        for event in events
        if is_in_interval(event["timestamp"], begin_date, end_date)
    ]

    count = len(events_found)

    return {"count": count, "events": events_found}, HTTPStatus.OK


@app.post("/h")
def create_event():
    expected_keys = {"timestamp", "description"}
    data = request.get_json()

    try:
        validate_keys(data, expected_keys)
    except KeyError as e:
        return e.args[0], HTTPStatus.BAD_REQUEST

    write_event_in_csv(data)

    return {"msg": "event created"}


@app.delete("/h/<event_id>")
def delete_event(event_id):
    events = read_events_from_csv()

    new_events = [event for event in events if event["id"] != event_id]

    rewrite_events_in_csv(new_events)

    return {"msg": "event deleted"}, HTTPStatus.OK


# TODO: PATCH
