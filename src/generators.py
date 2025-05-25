from typing import Generator

from typing import Iterator, List, Dict


def filter_by_currency(list_of_dicts: List[Dict], currency: str = "USD") -> Iterator[Dict]:
    """Функция для фильтрации транзакций по валюте"""
    def predicate(transaction):
        return transaction["operationAmount"]["currency"]["code"] == currency

    return filter(predicate, list_of_dicts)





def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генерирует номера карт в заданном диапазоне"""
    for number in range(start, stop):
        card_number = str(number).zfill(16)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"

