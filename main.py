import re
from collections import Counter
from typing import Dict, List

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_transaction_amount, load_transactions
from src.widget import get_date, mask_account_card


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка.
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [tx for tx in data if pattern.search(tx.get("description", ""))]


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    """
    counted: Dict[str, int] = Counter()
    for tx in data:
        description = tx.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                counted[category] += 1
    return dict(counted)


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями")
    print("Выберите необходимый пункт меню: ")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить инфорацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_map = {
        "1": (r"C:\Users\smotr\Desktop\Kurs2\data\operations.json"),
        "2": (r"C:\Users\smotr\Desktop\Kurs2\data\transactions.csv"),
        "3": (r"C:\Users\smotr\Desktop\Kurs2\data\transactions_excel.xlsx"),
    }

    while True:
        choice = input("Введите номер: ")
        if choice in file_map:
            print(f"Для обработки выбран файл: {file_map[choice]}")
            break
        print("Неверный выбор. Попробуйте снова")

    transactions = load_transactions(file_map[choice])
    print(f"Загружено: {len(transactions)} транзакций")

    while True:
        status = (
            input("Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): ")
            .strip()
            .upper()
        )
        if status in {"EXECUTED", "CANCELED", "PENDING"}:
            transactions = filter_by_state(transactions, status)
            print(f"Операции отфильтрованы по статусу {status}.")
            break
        else:
            print(f"Статус операции {status} недоступен.")

    sort = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort == "да":
        order = input("Отсортировать по убыванию или по возрастанию?: ").strip().lower()
        if order == "по возрастанию":
            reverse = False
        else:
            reverse = True

        transactions = sort_by_date(transactions, reverse=reverse)

    rub_only = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if rub_only == "да":
        transactions = list(filter_by_currency(transactions, "RUB"))

    search = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if search == "да":
        word = input("Введите слово для фильтра: ").strip().lower()
        transactions = process_bank_search(transactions, word)

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций: {len(transactions)}")

    for tx in transactions:
        date = get_date(tx.get("date", ""))
        description = tx.get("description", "Без описания")
        from_ = mask_account_card(tx.get("from")) if tx.get("from") else " "
        to = mask_account_card(tx.get("to")) if tx.get("to") else " "
        amount = get_transaction_amount(tx)
        currency = tx.get("operationAmount", {}).get("currency", {}).get("code", "")

        print(f"{date} {description}")
        if from_ and to:
            print(f"{from_} -> {to}")
        elif from_:
            print(from_)
        elif to:
            print(to)
        print(f"Сумма: {amount:.0f} {currency}")


if __name__ == "__main__":
    main()
