from csv import DictReader, DictWriter


def read_events_from_csv():
    with open("events.csv", "r") as csv_file:
        reader = DictReader(csv_file)
        events = list(reader)
        # print(f"{reader=}")
        # print(f"{reader.fieldnames=}")
        # print(f"{list(reader)=}")

        for event in events:
            for key, value in event.items():
                if key == "timestamp":
                    event[key] = float(value)

        return events


def write_event_in_csv(payload: dict):
    with open("events.csv", "a") as csv_file:
        fieldnames = ["id", "description", "timestamp"]
        writer = DictWriter(csv_file, fieldnames)

        writer.writerow(payload)


def rewrite_events_in_csv(payload: list[dict]):
    with open("events.csv", "w") as csv_file:
        fieldnames = ["id", "description", "timestamp"]

        writer = DictWriter(csv_file, fieldnames)

        writer.writeheader()
        writer.writerows(payload)
