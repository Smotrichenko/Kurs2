import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(transactions):
    result = filter_by_currency(transactions, "USD")
    for trans in result:
        assert trans["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_none(transactions):
    result = list(filter_by_currency(transactions, "EUR"))
    assert result == []


def test_filter_by_currency_empty():
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions(transactions):
    result = list(transaction_descriptions(transactions))
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
    ]


def test_transaction_descriptions_empty():
    result = list(transaction_descriptions([]))
    assert result == []


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011"]),
        (1000, 1001, ["0000 0000 0000 1000"]),
    ],
)
def test_card_number_generator(start, end, expected):
    result = list(card_number_generator(start, end))
    assert result == expected


def test_card_number_generator_empty_range():
    result = list(card_number_generator(5, 5))
    assert result == []
