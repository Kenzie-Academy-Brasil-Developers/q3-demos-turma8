from flask import Flask, request
from datetime import datetime as dt
from http import HTTPStatus

from .database.historical_events_database import historical_events

app = Flask(__name__)


@app.get('/h')
def home():
    return historical_events, 200


@app.get('/h/1702')
def retrive_1702():

    events_found = [
        event
        for event in historical_events['result']
        if dt.fromtimestamp(event['timestamp']).year == 1702
    ]

    count = len(events_found)

    return {'count': count, 'events': events_found}, 200


@app.get('/h/<int:year>')
def retrive_by_year(year):

    # year = int(year)
    # print(f'{year=}')
    # print(f'{type(year)=}')

    events_found = [
        event
        for event in historical_events['result']
        if dt.fromtimestamp(event['timestamp']).year == year
    ]

    count = len(events_found)

    return {'count': count, 'events': events_found}, 200


@app.get('/h/day/<int:day>')
def retrive_by_day(day):

    events_found = [
        event
        for event in historical_events['result']
        if dt.fromtimestamp(event['timestamp']).day == day
    ]

    count = len(events_found)

    return {'count': count, 'events': events_found}, 200


@app.get('/h/query')
def retrieve_by_date_interval():
    # print(f'{request.args["begin_date"]=}')

    begin_date = request.args.get('begin_date')
    end_date = request.args.get('end_date')

    if not begin_date or not end_date:
        return {'error': 'you must pass a begin and end date'}, HTTPStatus.BAD_REQUEST

    events_found = []

    begin_date_object = dt.strptime(begin_date, '%Y-%m-%d')
    end_date_object = dt.strptime(end_date, '%Y-%m-%d')

    for event in historical_events['result']:
        print(f'{event=}')
        event_date = dt.fromtimestamp(event["timestamp"])

        if begin_date_object <= event_date <= end_date_object:
            event_formated_date = event_date.strftime('%Y-%m-%d')
            event['formated_date'] = event_formated_date
            # event['formated_date'] = event_date
            event.pop('timestamp')
            events_found.append(event)

    count = len(events_found)

    return {'count': count, 'events': events_found}, 200
