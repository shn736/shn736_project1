from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card: str) -> str:
    """функция которая обрабатывауе информацию как о картах, так и о счетах"""
    len_account = ''.join(number for number in account_card if number.isdigit())
    if "Счет" in account_card:
        if len(len_account) != 20:
            return "Вы ввели не верный номер счета"
        else:
            return f"{account_card[:5]}{get_mask_account(account_card[-20:])}"
    else:
        if len(len_account) != 16:
            return "Вы ввели не верный номер счета"
        else:
            return f"{account_card[:-16]}{get_mask_card_number(account_card[-16:])}"


mask_account_card(account_card='Счет 73654108430135874305')


def get_date(date: str) -> str:
    """возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    entered_day = date[8: 10]
    entered_month  = date[5: 7]
    entered_year = {date[0: 4]}
    if date is None:
        return "Некорректный ввод"
    else:
        is_digit_present = any(character.isdigit() for character in date)
        if is_digit_present != True:
            return "Некорректный ввод"
        elif int(entered_day) > 31:
            return "Некорректный ввод"
        else:
            return f"{date[8: 10]}.{date[5: 7]}.{date[0: 4]}"


get_date(date='2024-03-11T02:26:18.671407')
