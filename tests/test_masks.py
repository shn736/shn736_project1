from src.masks import get_mask_card_number, get_mask_account


def tests_get_mask_card_number():
    assert get_mask_card_number(card_number='7000792289606361') == '7000 79** **** 6361'


def tests_len_get_mask_card_number():
    assert get_mask_card_number(card_number='700079228911606361') == "Вы ввели не верный номер карты"


def tests_get_mask_card_number_empty():
    assert get_mask_card_number(card_number=' ') == "Вы ввели не верный номер карты"


def tests_get_mask_account():
    assert get_mask_account(account='73654108430135874305') == '**4305'


def tests_get_mask_account_empty():
    assert get_mask_account(account=' ') == 'Вы ввели не верный номер счета'


def tests_shorter_len_get_mask_account():
    assert get_mask_account(account='73654108430174305') == 'Вы ввели не верный номер счета'


def tests_longer_len_get_mask_account():
    assert get_mask_account(account='7365410843011111111174305') == 'Вы ввели не верный номер счета'
