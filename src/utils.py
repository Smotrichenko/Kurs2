import json
from typing import List


def load_transactions(filename):
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

transactions = load_transactions(r"C:\Users\smotr\Desktop\Kurs2\data\operations.json")
print(transactions)
