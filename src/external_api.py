import datetime
import os
from dotenv import load_dotenv
import requests

from src.utils import operations_list

load_dotenv('.env')

API_KEY = os.getenv('API_KEY')

transactions = operations_list('operations.json')


def sum_transactions(transactions):
    """Функция, которая принимает на вход транзакцию и возвращает
    сумму транзакций (amount) в рублях, тип данных — float"""
    for i in transactions:
        if i == {}:
            print("Произошла ошибка!")
        else:
            to = "RUB"
            from_1 = "USD"
            from_2 = "EUR"
            value = float(i["operationAmount"]["amount"])
            if i["operationAmount"]["currency"]["code"] == "RUB":
                result = float(i["operationAmount"]["amount"])
                return result
            else:
                if i["operationAmount"]["currency"]["code"] == "USD":
                    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_1}&amount={value}"
                    headers = {"apikey": API_KEY}
                    response = requests.request("GET", url, headers=headers)
                    convert_amount = response.json()
                    result = convert_amount["result"]
                    return result
                else:
                    if i["operationAmount"]["currency"]["code"] == "EUR":
                        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_2}&amount={value}"
                        headers = {"apikey": API_KEY}
                        response = requests.request("GET", url, headers=headers)
                        convert_amount = response.json()
                        result = convert_amount["result"]
                        return result
