import pytest


from src.masks import get_mask_card_number, get_mask_account


def tests_get_mask_card_number() -> None:
    assert get_mask_card_number(card_number='7000792289606361') == '7000 79** **** 6361'


def tests_len_get_mask_card_number() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number='700079228911606361')


def tests_get_mask_card_number_empty() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number=' ')


def tests_get_mask_account() -> None:
    assert get_mask_account(account='73654108430135874305') == '**4305'


def tests_len_long_get_mask_account() -> None:
    with pytest.raises(ValueError):
        get_mask_account(account='7365410843011111111174305')


def tests_len_short_get_mask_account() -> None:
    with pytest.raises(ValueError):
        get_mask_account(account='73654108430174305')


def tests_len_empty_get_mask_account() -> None:
    with pytest.raises(ValueError):
        get_mask_account(account=' ')
