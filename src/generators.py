from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Генератор, который поочередно возвращает транзакции,
    в которых код валюты совпадает с currency_code.
    """
    for transaction in transactions:
        currency = transaction["operationAmount"]["currency"]["code"]
        if currency == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[Dict[str, Any]]:
    """
    Генератор,  который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди.
    """

    for transaction in transactions:
        description = transaction["description"]
        yield description


def card_number_generator(start: int, end: int) -> Iterator:
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    в диапазоне от start до end.
    """
    for num in range(start, end):
        num_str = f"{num:016d}"
        formatted = " ".join([num_str[i: i + 4] for i in range(0, 16, 4)])
        yield formatted
