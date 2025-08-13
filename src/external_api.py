import logging
import os
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

log_file_path = os.path.join(LOG_DIR, "utils.log")
logger = logging.getLogger("API")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file_path, mode='w', encoding="utf=8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def convert_to_rub(operation_amount: Dict) -> float:
    """
    Конвертирует сумму из валюты currency в рубли с использованием внешнего API.
    """
    try:
        amount = float(operation_amount.get("amount", 0.0))
        currency = operation_amount.get("currency", {}).get("code", "RUB")

        if currency == "RUB":
            return amount

        headers = {"apikey": API_KEY}

        params = {"from": currency, "to": "RUB", "amount": amount}

        response = requests.get(BASE_URL, headers=headers, params=params)
        if response.status_code != 200:
            raise ValueError(f"Ошибка при запуске курса валют: {response.text}")

        data = response.json()
        logger.debug("Конвертация прошла успешно")
        return float(data.get("result", 0.0))
    except (requests.RequestException, Exception) as ex:
        logger.error(f"Произошла ошибка: {ex}")
        print(f"Ошибка при конвертации валюты: {ex}")
        return 0.0
