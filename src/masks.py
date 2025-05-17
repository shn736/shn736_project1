def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    if len(card_number) != 16:
        return "Вы ввели не верный номер карты"

    else:
        return f"{card_number[0: 4]} {card_number[4: 6]}** ****  {card_number[-4:]}"


get_mask_card_number(card_number='7000792289606361')


def get_mask_account(account: str) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    if len(account) != 20:
        return "Вы ввели не верный номер счета"

    else:
        return f"**{account[-4:]}"


get_mask_account(account='73654108430135874305')
