import os
from dotenv import load_dotenv
import requests


load_dotenv('.env')

API_KEY = os.getenv('API_KEY')


def sum_transactions(transaction):
    """Функция, которая принимает на вход транзакцию и возвращает
    сумму транзакций (amount) в рублях, тип данных — float"""
    if transaction == {}:
        print("Произошла ошибка!")
    else:
        to = "RUB"
        from_1 = "USD"
        from_2 = "EUR"
        value = float(transaction["operationAmount"]["amount"])
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            result = float(transaction["operationAmount"]["amount"])
            return result
        else:
            if transaction["operationAmount"]["currency"]["code"] == "USD":
                url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_1}&amount={value}"
                headers = {"apikey": API_KEY}
                response = requests.get(url, headers=headers)
                convert_amount = response.json()
                result = convert_amount['result']
                print(type(result))
                return result
            else:
                if transaction["operationAmount"]["currency"]["code"] == "EUR":
                    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_2}&amount={value}"
                    headers = {"apikey": API_KEY}
                    response = requests.get(url, headers=headers)
                    convert_amount = response.json()
                    result = convert_amount['result']
                    return result
