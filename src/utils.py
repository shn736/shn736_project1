import json

from typing import Any


def operations_list(path: str) -> Any:
    try:
        with open('operations.json', encoding='utf-8') as json_file:
            operation_str = json.load(json_file)
            return operation_str
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return[]

#
