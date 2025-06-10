from unittest.mock import patch
from src.external_api import sum_transactions
import os
from dotenv import load_dotenv
load_dotenv('.env')

API_KEY = os.getenv('API_KEY')

transaction_usd = {
                    'id': 716496732, 'state': 'EXECUTED', 'date': '2018-04-04T17:33:34.701093', 'operationAmount':
                    {'amount': '40701.91', 'currency': {'name': 'USD', 'code': 'USD'}}
                  }


@patch("requests.get")
def test_sum_transactions_usd(mock_get):
    headers = {"apikey": API_KEY}
    url = (
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from="
            f"{transaction_usd['operationAmount']['currency']['code']}&amount="
            f"{transaction_usd['operationAmount']['amount']}"
    )
    mock_get.return_value.json.return_value = {'result': 3197431.543914}
    result = sum_transactions(transaction_usd)
    assert result == 3197431.543914
    mock_get.assert_called_once_with(url, headers=headers)


transaction_eur = {'id': 716496732, 'state': 'EXECUTED', 'date': '2018-04-04T17:33:34.701093',
                   'operationAmount': {'amount': '40701.91', 'currency': {'name': 'EUR', 'code': 'EUR'}}}


@patch("requests.get")
def test_sum_transactions_eur(mock_get):
    headers = {"apikey": API_KEY}
    url = (
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from="
        f"{transaction_eur['operationAmount']['currency']['code']}&amount="
        f"{transaction_eur['operationAmount']['amount']}"
    )
    mock_get.return_value.json.return_value = {'result': 3646496.001858}
    result = sum_transactions(transaction_eur)
    assert result == 3646496.001858
    mock_get.assert_called_once_with(url, headers=headers)


transaction_rub = {'id': 716496732, 'state': 'EXECUTED', 'date': '2018-04-04T17:33:34.701093',
                   'operationAmount': {'amount': '40701.91', 'currency': {'name': 'RUB', 'code': 'RUB'}}}


@patch("requests.get")
def test_sum_transactions_rub(mock_get):
    mock_get.return_value.json.return_value = {'result': 40701.91}
    result = sum_transactions(transaction_rub)
    assert result == 40701.91
