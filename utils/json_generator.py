from json import dump


def save_as_json(path: str, data: dict) -> None:
    with open(path, 'w') as write:
        dump(data, write)
