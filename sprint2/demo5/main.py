from csv import DictWriter

from demo5.database.historical_events_database import historical_events

FILEPATH = "events.csv"


def normalize_events(events: list, wanted_keys: list):
    for index, event in enumerate(events, 1):
        for key in list(event.keys()).copy():
            if key not in wanted_keys:
                event.pop(key)

            # event["id"] = index
            event.update({"id": index})
    # return events


def write_events_in_csv():
    # Equivalentes
    # csv_file = open('events.csv', "w")
    events = historical_events["result"]
    fieldnames = ["id", "description", "timestamp"]

    normalize_events(events, fieldnames)

    csv_file = open(FILEPATH, "w")

    writer = DictWriter(csv_file, fieldnames)

    writer.writeheader()
    writer.writerows(events)

    csv_file.close()


write_events_in_csv()
