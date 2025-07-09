from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Генератор, который поочередно возвращает транзакции,
    в которых код валюты совпадает с currency.
    """
    for transaction in transactions:
        currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        if currency == currency_code:
            yield transaction


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 123456789,
        "state": "EXECUTED",
        "date": "2021-07-15T10:00:00.000000",
        "operationAmount": {"amount": "5000.00", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 12345678901234567890",
        "to": "Счет 09876543210987654321",
    },
]

usd_transactions_gen = filter_by_currency(transactions, "USD")
for i in range(3):
    try:
        result = next(usd_transactions_gen)
        print(result)
    except StopIteration:
        print("Все транзакции с USD выведены")
        break
