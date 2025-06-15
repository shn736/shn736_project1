import csv
import pandas as pd
from typing import Any


def reading_operations_csv(transactions_csv: str) -> Any:
    """считывает финансовые операции из CSV выдает список словарей с транзакциями"""
    list_transactions_csv = []
    try:
        with open(transactions_csv) as trans_file:
            reader = csv.DictReader(trans_file)
            for row in reader:
                list_transactions_csv.append(row)
            return list_transactions_csv
    except FileNotFoundError:
        return f"Ошибка: Файл по пути '{transactions_csv}' не найден."
    except Exception as e:
        return f"Произошла ошибка: {e}"


def reading_operations_excel(transactions_excel: str) -> Any:
    """считывает финансовые операции из Excel выдает список словарей с транзакциями"""
    try:
        df = pd.read_excel(transactions_excel)
        list_transaction_excel = df.to_dict(orient='records')
        return list_transaction_excel
    except FileNotFoundError:
        return f"Ошибка: Файл не найден по указанному пути: {transactions_excel}"
    except ValueError:
        return "Ошибка: Не удалось прочитать файл. Убедитесь, что это файл Excel."
    except Exception as e:
        return f"Произошла ошибка: {e}"
