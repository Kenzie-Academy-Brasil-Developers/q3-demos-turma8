from datetime import datetime as dt


def is_in_interval(timestamp: float, begin: str, end: str):
    begin_date_object = dt.strptime(begin, "%Y-%m-%d")
    end_date_object = dt.strptime(end, "%Y-%m-%d")
    event_date = dt.fromtimestamp(timestamp)

    return begin_date_object <= event_date <= end_date_object


def serialize_event(event: dict):
    event["date"] = dt.fromtimestamp(event["timestamp"]).strftime("%Y-%m-%d")
    event.pop("timestamp")

    return event


# TODO: Criar condição para avaliar quando o usuário passa apenas 1 chave válida
def validate_keys(payload: dict, expected_keys: set):
    body_keys_set = set(payload.keys())

    invalid_keys = body_keys_set - expected_keys

    if invalid_keys:
        raise KeyError(
            {
                "error": "invalid_keys",
                "expected": list(expected_keys),
                "received": list(body_keys_set),
            }
        )
