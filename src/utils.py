import json
import logging
import os
from json import JSONDecodeError
from typing import Any, Dict, List

from src.external_api import convert_to_rub

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

log_file_path = os.path.join(LOG_DIR, "utils.log")
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file_path, mode='w', encoding="utf=8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(filename: Any) -> List:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях.
    """
    try:
        logger.debug("Открываем файл JSON")
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, List):
                return data
            else:
                print("Ожидается список транзакций в JSON-файле")
                return []
    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        print(f"Файл по пути {filename} не найден")
        return []
    except JSONDecodeError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        print(f"Ошибка чтения JSON в файле {filename}")
        return []


def get_transaction_amount(transactions: Dict[str, Any]) -> float:
    """
    Принимает транзакцию и возвращает сумму в рублях.
    Если валюта не рубль — конвертирует через внешний API.
    """
    try:
        logger.debug(f'Принимаем транзакцию {transactions.get("id")}')
        operation_amount = transactions.get("operationAmount")
        if not operation_amount or not isinstance(operation_amount, dict):
            return 0.0
        currency = operation_amount.get("currency", {}).get("code", "RUB")
        if currency == "RUB":
            return float(operation_amount.get("amount", 0.0))

        logger.debug("Конвентируем через внешний API")
        return convert_to_rub(operation_amount)

    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return 0.0


transactions = load_transactions(r"C:\Users\smotr\Desktop\Kurs2\data\operations.json")

for i in transactions:
    if not i or "operationAmount" not in i:
        continue
    rub_amount = get_transaction_amount(i)
    print(f"Транзакция {i['id']}: {rub_amount:.2f} RUB")
