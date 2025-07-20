import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rub(amount: float, currency: str) -> float:
    """
    Конвертирует сумму из валюты currency в рубли с использованием внешнего API.
    """
    if currency == "RUB":
        return amount

    headers = {"apikey": API_KEY}

    params = {"from": currency, "to": "RUB", "amount": amount}

    response = requests.get(BASE_URL, headers=headers, params=params)
    if response.status_code != 200:
        raise ValueError(f"Ошибка при запуске курса валют: {response.text}")

    data = response.json()
    return float(data.get("result", 0.0))
