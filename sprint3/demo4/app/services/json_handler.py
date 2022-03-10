import json
# json.decoder.JSONDecodeError
from json import JSONDecodeError


def read_json(filepath: str) -> list:
    try:
        with open(filepath, "r") as json_file:
            return json.load(json_file)
    except (FileNotFoundError, JSONDecodeError):
        return []


def write_json(filepath: str, payload: dict):
    json_list = read_json(filepath)
    json_list.append(payload)

    print(f"{json_list=}")

    with open(filepath, "w") as json_file:
        json.dump(json_list, json_file, indent=2)

        return payload
