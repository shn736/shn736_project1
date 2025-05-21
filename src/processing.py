from typing import List, Dict, Any


def filter_by_state(transactions: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """Функция возвращает новый список, отфильтрованный по указанному значению"""
    return [item for item in transactions if item.get("state") == state]


def sort_by_date(operations: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция возвращает новый список, отсортированный по дате"""
    return sorted(operations, key=lambda x: x.get(str('date')), reverse=reverse)
