def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    if len(card_number) != 16:
        raise ValueError("Вы ввели не верный номер карты")

    else:
        return f"{card_number[0: 4]} {card_number[4: 6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    if len(account) != 20:
        raise ValueError("Вы ввели не верный номер счета")

    else:
        return f"**{account[-4:]}"
