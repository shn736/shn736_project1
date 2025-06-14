import csv
import pandas as pd


def reading_operations_csv(transactions_csv):
    list_transactions_csv = []
    try:
        with open(transactions_csv) as trans_file:
            reader = csv.DictReader(trans_file)
            for row in reader:
                list_transactions_csv.append(row)
            return list_transactions_csv
    except FileNotFoundError:
        return f"Ошибка: Файл по пути '{transactions_csv}' не найден."
    except csv.Error as e:
        return f"Ошибка при чтении CSV файла: {e}"
    except Exception as e:
        return f"Произошла ошибка: {e}"


def reading_operations_excel(transactions_excel):
    try:
        # Чтение Excel файла
        df = pd.read_excel(transactions_excel)

        # Преобразование DataFrame в список словарей
        transactions = df.to_dict(orient='records')

        return transactions
    except FileNotFoundError:
        return f"Ошибка: Файл не найден по указанному пути: {transactions_excel}"
    except ValueError:
        return "Ошибка: Не удалось прочитать файл. Убедитесь, что это файл Excel."
    except Exception as e:
        return f"Произошла ошибка: {e}"



