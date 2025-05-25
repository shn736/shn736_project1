import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def transactions_list():
    return (
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"
            },
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {
                    "amount": "43318.34",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160"
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {
                    "amount": "56883.54",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229"
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"
            }
        ]
    )


def test_transaction_descriptions(transactions_list):
    generator = transaction_descriptions(transactions_list)
    assert next(generator) == 'Перевод организации'
    assert next(generator) == 'Перевод со счета на счет'
    assert next(generator) == 'Перевод со счета на счет'
    assert next(generator) == 'Перевод с карты на карту'
    assert next(generator) == 'Перевод организации'


def test_card_number_generator(start=1, stop=5):
    generator = card_number_generator(start=1, stop=5)
    assert next(generator) == '0000 0000 0000 0001'
    assert next(generator) == '0000 0000 0000 0002'
    assert next(generator) == '0000 0000 0000 0003'
    assert next(generator) == '0000 0000 0000 0004'


def test_empty_transactions_list():
    """Тестируем кейс с пустым списком на входе"""
    assert list(filter_by_currency(transactions=[], currency="USD")) == list([])


def test_with_not_exist_money(transactions_list):
    """Тестируем кейс с запросом выборки в валюте, транзакций по которой нет в списке"""
    result = filter_by_currency(transactions_list, currency="UAH")
    with pytest.raises(StopIteration):
        next(result)


@pytest.mark.parametrize(
    "value, expected",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                }
            ],
        ),
        (
            "RUB",
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                }
            ]
        ),
    ],
)
def test_filter_by_currency_value(transactions_list, value, expected):
    assert list(filter_by_currency(transactions_list, value)) == expected


def test_filter_by_currency_usd(transactions_list):
    generator = filter_by_currency(transactions_list, currency="USD")
    assert next(generator) == {
        'id': 939719570, 'state': 'EXECUTED', 'date':
        '2018-06-30T02:08:58.425572', 'operationAmount':
        {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
        'description': 'Перевод организации', 'from':
        'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}
    assert next(generator) == {
        'id': 142264268, 'state': 'EXECUTED', 'date':
        '2019-04-04T23:20:05.206878', 'operationAmount':
        {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
        'description': 'Перевод со счета на счет', 'from':
        'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}


def test_filter_by_currency_rub(transactions_list):
    generator = filter_by_currency(transactions_list, currency="RUB")
    assert next(generator) == {
        'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404', 'operationAmount':
        {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},
        'description': 'Перевод со счета на счет', 'from':
        'Счет 44812258784861134719', 'to': 'Счет 74489636417521191160'}
    assert next(generator) == {
        'id': 594226727, 'state': 'CANCELED', 'date':
        '2018-09-12T21:27:25.241689', 'operationAmount':
        {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}},
        'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588',
        'to': 'Счет 14211924144426031657'}
