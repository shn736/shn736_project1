# import json
# import pandas as pd
from src.reading_operations import reading_operations_excel, reading_operations_csv

from src.utils import operations_list

from src.processing import filter_by_state, sort_by_date

from src.generators import filter_by_currency
from src.widget import get_date, mask_account_card


def main():
    global filtered_transactions_currency
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    file_choices = {
        "1": "json",
        "2": "csv",
        "3": "xlsx"
    }

    file_choice = input(
        "Выберите необходимый пункт меню:\n1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла\n")

    file_type = file_choices.get(file_choice)
    if file_type == "json":
        data = operations_list(path='../data/operations.json')
        print(data)
    elif file_type == "csv":
        data = reading_operations_csv(transactions_csv = '../data/transactions.csv')
        print(data)
    elif file_type == "xlsx":
        data = reading_operations_excel(transactions_excel='../data/transactions_excel.xls')
    else:
        print("Некорректный выбор. Программа завершена.")
        return


    status = input(
        "Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").strip().lower()

    while status not in ['executed', 'canceled', 'pending']:
        print(f"Статус операции \"{status}\" недоступен.")

    filtered_transactions = filter_by_state(transactions = data , state = status.upper())

    print(f"Операции отфильтрованы по статусу \"{status.upper()}\".")
    print(filtered_transactions)
    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    sort_choice = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
    if sort_choice == 'да':
        order_choice = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
        if order_choice == 'по возрастанию':
            filtered_transactions = sort_by_date(operations=filtered_transactions, reverse=True)
        elif order_choice == 'по убыванию':
            filtered_transactions = sort_by_date(operations=filtered_transactions, reverse=False)
    elif sort_choice == 'нет':
        filtered_transactions = filtered_transactions
    filtered_transactions_date = filtered_transactions
    print(filtered_transactions_date)
    rub_choice = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
    if rub_choice == 'да':
        filtered_transactions_currency = []
        for transaction in filter_by_currency(transactions=filtered_transactions_date, currency='RUB'):
            filtered_transactions_currency.append(transaction)
            print(filtered_transactions_currency)
    elif rub_choice == 'нет':
        filtered_transactions_currency=filtered_transactions_date
        print(filtered_transactions_currency)

    filter_word_choice = input(
         "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
    if filter_word_choice == 'да':
         word = input("Введите слово для фильтрации по описанию:\n").strip().lower()
         filtered_transactions = [txn for txn in filtered_transactions_currency if word in txn['description'].lower()]
    else:
        filtered_transactions = filtered_transactions_currency

    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}\n")

    for txn in filtered_transactions:

        if file_type == "json" or file_type == "csv":
            summ = txn['operationAmount']['amount']
            code_currency = txn['operationAmount']['currency']['code']
            if txn['description'] == 'Перевод организации' or txn['description'] == 'Перевод с карты на карту' or txn['description'] == 'Перевод со счета на счет':
                print(f"{get_date(txn['date'])} {txn['description']}\n"
                    f"{mask_account_card(txn['from'])} -> {mask_account_card(txn['to'])}\n"
                    f"Сумма: {summ} {code_currency}\n")
            else:
                print(f"{get_date(txn['date'])} {txn['description']}\n"
                 f"{mask_account_card(txn['to'])}\n"
                 f"Сумма: {summ} {code_currency}\n")
        elif file_type == "xlsx":
            if txn['description'] == 'Перевод организации' or txn['description'] == 'Перевод с карты на карту' or txn['description'] == 'Перевод со счета на счет':
                print(f"{get_date(txn['date'])} {txn['description']}\n"
            f"{mask_account_card(txn['from'])} -> {mask_account_card(txn['to'])}\n"
            f"Сумма: {txn['amount']} {txn['currency_code']}\n")
            else:
                print(f"{get_date(txn['date'])} {txn['description']}\n"
                f"{mask_account_card(txn['to'])}\n"
                f"Сумма: {txn['amount']} {txn['currency_code']}\n")


if __name__ == "__main__":
    main()