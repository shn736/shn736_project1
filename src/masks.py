import logging


# logging.basicConfig(encoding='utf-8')
# logger = logging.getLogger('masks')
# logger.setLevel(logging.DEBUG)
# file_handler = logging.FileHandler('logs/masks.log')
# file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    if len(card_number) != 16:
        #logger.error('Произошла ошибка: Вы ввели не верный номер карты')
        raise ValueError("Вы ввели не верный номер карты")

    else:
        #logger.info('Возвращена маска номера карты')
        return f"{card_number[0: 4]} {card_number[4: 6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    if len(account) != 20:
        #logger.error('Произошла ошибка: Вы ввели не верный номер счета')
        raise ValueError("Вы ввели не верный номер счета")

    else:
        #logger.info('Возвращена маска номера счета')
        return f"**{account[-4:]}"
