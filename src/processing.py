transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(transactions: list[dict[str, any]], state: str = 'EXECUTED') -> list[dict]:
    """Функция возвращает новый список, отфильтрованный по указанному значению"""
    return [item for item in transactions if item.get("state") == state]


print(filter_by_state(transactions, "EXECUTED"))


operations = [
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]


def sort_by_date(operations: list[dict[str, any]], reverse: bool = True) -> list[dict]:
    """Функция должна возвращает новый список, отсортированный по дате"""
    return sorted(operations, key=lambda x: x.get("date"), reverse=reverse)


print(sort_by_date(operations))
