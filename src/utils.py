import json
from typing import Any
import logging


logging.basicConfig(encoding='utf-8')
logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/utils.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def operations_list(path: str) -> Any:
    """функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding='utf-8') as json_file:
            operation_str = json.load(json_file)
            logger.info('Возвращен список словарей')
            return operation_str
    except json.JSONDecodeError:
        logger.error('Неправильная структура JSON')
        return []
    except FileNotFoundError:
        logger.error('Файл не существует в указанном месте')
        return []
