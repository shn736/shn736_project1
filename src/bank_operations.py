import re

from src.reading_operations import reading_operations_excel

data = reading_operations_excel(transactions_excel='../data/transactions_excel.xls')
search_string = 'Перевод'
categories = ['Перевод с карты на карту', 'Перевод со счета на счет']


def search_transactions(data, search_string):
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    filtered_transactions = []
    for transaction in data:
        if isinstance(transaction.get('description', ''), str):
            if pattern.search(transaction.get('description', '')):
                filtered_transactions.append(transaction)
    return filtered_transactions


def count_transactions_by_category(data, categories):
    category_count = {category: 0 for category in categories}
    for transaction in data:
        category = transaction.get('description')
        if category in category_count:
            category_count[category] += 1

    return category_count
