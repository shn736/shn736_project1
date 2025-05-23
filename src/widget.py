from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card: str) -> str:
    """функция которая обрабатывауе информацию как о картах, так и о счетах"""
    if "Счет" in account_card:
        return f"{account_card[:5]}{get_mask_account(account_card[-20:])}"
    else:
        return f"{account_card[:-16]}{get_mask_card_number(account_card[-16:])}"


mask_account_card(account_card='Счет 73654108430135874305')


def get_date(date: str) -> str:
    """возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    return f"{date[8: 10]}.{date[5: 7]}.{date[0: 4]}"


get_date(date='2024-03-11T02:26:18.671407')
