from collections import Counter
from typing import Any


def count_transactions(transactions: dict[list]) -> dict[Any, int]:
    """Подсчитывает количество банковских операций определенного типа."""

    count_dict = {}
    descriptions = [transaction['description'] for transaction in transactions]
    counter = Counter(descriptions)
    for description, count in counter.items():
        count_dict[description] = count

    return count_dict
