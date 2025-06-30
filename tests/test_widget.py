import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("", "Некорректный ввод"),
        ("MasterCard7158300734726758", "Некорректный ввод"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счёт 73654108430135874305", "Счет **4305"),
        ("Visa Platinum", "Некорректный номер карты"),
        ("None", "Некорректный ввод"),
        ("Visa Platinum qwerty", "Некорректный номер карты"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "input_date,expected_output",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("1999-12-31T23:59:59", "31.12.1999"),
        ("2024-03-11", "11.03.2024"),
        ("", "Некорректная дата"),
        (None, "Некорректная дата"),
        ("не дата", "Некорректная дата"),
        ("2024-02-30T00:00:00", "Некорректная дата"),
    ]
)
def test_get_date(input_date, expected_output):
    assert get_date(input_date) == expected_output
