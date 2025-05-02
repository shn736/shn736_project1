def mask_account_card(account_card: str) -> str:
    """функция которая обрабатывауе информацию как о картах, так и о счетах"""
    if "Счет" in account_card:
        return f"{account_card[:5]} **{account_card[-20: -16]}"
    else:
        return f"{account_card[:-16]}{account_card[-16:-12]} {account_card[-12:-10]}** **** {account_card[-4:]}"


print(mask_account_card(account_card='Visa Platinum 7000792289606361'))

def get_date(date: str) -> str:
    """возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    return f" {date[8: 10]}.{date[5: 7]}.{date[0: 4]}"

print(get_date(date='2024-03-11T02:26:18.671407'))
