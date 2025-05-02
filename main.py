from src.masks import get_mask_card_number, get_mask_account

from src.widget import mask_account_card, get_date

print(get_mask_card_number(card_number='7000792289606361'))

print(get_mask_account(account='73654108430135874305'))

print(mask_account_card(account_card='Visa Platinum 7000792289606361'))

print(get_date(date='2024-03-11T02:26:18.671407'))
