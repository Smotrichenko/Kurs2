import json
from typing import Any, Dict, List

from src.external_api import convert_to_rub


def load_transactions(filename: Any) -> List:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, List):
                return data
            else:
                print("Ожидается список транзакций в JSON-файле")
                return []
    except FileNotFoundError:
        print(f"Файл по пути {filename} не найден")
        return []


def get_transaction_amount(transactions: Dict[str, Any]) -> float:
    """
    Принимает транзакцию и возвращает сумму в рублях.
    Если валюта не рубль — конвертирует через внешний API.
    """
    amount = float(transactions["operationAmount"]["amount"])
    currency = transactions["operationAmount"]["currency"]["code"]
    return convert_to_rub(amount, currency)


transactions = load_transactions(r"C:\Users\smotr\Desktop\Kurs2\data\operations.json")

for i in transactions:
    if not i or "operationAmount" not in i:
        continue
    rub_amount = get_transaction_amount(i)
    print(f"Транзакция {i['id']}: {rub_amount:.2f} RUB")
