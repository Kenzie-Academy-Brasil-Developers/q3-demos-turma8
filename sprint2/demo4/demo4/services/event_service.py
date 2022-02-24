from datetime import datetime as dt


def is_in_interval(timestamp: float, begin: str, end: str):
    begin_date_object = dt.strptime(begin, '%Y-%m-%d')
    end_date_object = dt.strptime(end, '%Y-%m-%d')
    event_date = dt.fromtimestamp(timestamp)

    return begin_date_object <= event_date <= end_date_object


def serialize_event(event: dict):
    event['date'] = dt.fromtimestamp(event['timestamp']).strftime("%Y-%m-%d")
    event.pop("timestamp")

    return event
