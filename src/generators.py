from typing import Generator, Iterator, List, Dict


def filter_by_currency(transactions: List[Dict], currency: str = "USD") -> Iterator[Dict]:
    """Функция для фильтрации транзакций по валюте"""
    for transaction in transactions:
        if transactions is None:
            raise ValueError("Некорректный ввод")
        elif transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction



def transaction_descriptions(transaction_list: List[Dict]) -> Generator[str, None, None]:
    """Функция возвращает описание каждой операции по очереди"""
    for transaction in [t["description"] for t in transaction_list]:
        yield transaction


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генерирует номера карт в заданном диапазоне"""
    for number in range(start, stop):
        card_number = str(number).zfill(16)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
