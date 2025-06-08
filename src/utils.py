import json
from typing import Any

operations_file = '../data/operations.json'

def operations_list(path: str) -> Any:
    """функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(operations_file, encoding='utf-8') as json_file:
            operation_str = json.load(json_file)
            return operation_str
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
