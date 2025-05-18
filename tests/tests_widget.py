import pytest


from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "value_card_and_account, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
     ],
)


def test_positive_mask_account_card(value_card_and_account,expected_result):
    assert mask_account_card(value_card_and_account) == expected_result


@pytest.fixture
def wrong_card_and_account():
    return [
        "Счет 3538303347444789556001",
        "Счет ",
        "Visa Classic 700079228960636100",
        "Maestro 700079228960",
        "Visa Classic 7000 79** **** 6361",
        "Visa Platinum 65679228960099X",
        "MasterCard ?#656922860099_",
    ]


def tests_wrong_mask_account_card(wrong_card_and_account):
    assert mask_account_card(wrong_card_and_account) == "Вы ввели не верный номер счета"


@pytest.mark.parametrize(
    "incoming_date_time, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("1997-12-01T02:26:18.1", "01.12.1997"),
        (None, "Некорректный ввод"),
        ("", "Некорректный ввод"),
    ],
)
def test_positive_get_date(incoming_date_time, expected):
    assert get_date(incoming_date_time) == expected

@pytest.mark.parametrize(
    "incorrect_date_time",
    [
        ("0000-12-01T02:26:18.1"),
        ("year"),
        ("2024-03-11T02"),
        ("2024-00-11T02:26:18.671407"),
        ("??24-03-11T02:26:18.671407"),
        ("2024-03-00T02:26:18.671407"),
        ("2024-03-11"),
    ],
)
def test_errors_get_date(incorrect_date_time):
    # with pytest.raises(ValueError):
    #     get_date(incorrect_date_time)
    assert get_date(incorrect_date_time) is None