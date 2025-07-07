import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "original, expected",
    [
        ("2200701052954101", "2200 70** **** 4101"),
        ("220070105295410", "Недостаточная длина номера карты"),
        ("22007010529541012", "Слишком длинный номер карты"),
        ("2200701oo2954101", "Номер счета должен содержать только цифры"),
        ("", "Введите номер карты"),
    ],
)
def test_get_mask_card_number(original: str, expected: str) -> None:
    assert get_mask_card_number(original) == expected


@pytest.mark.parametrize(
    "original, expected",
    [
        ("40817810900111108057", "**8057"),
        ("4081781090011110805", "Введите 20-значный номер счета"),
        ("408178109001111080570", "Введите 20-значный номер счета"),
        ("4081781090011ll08057", "Номер счета должен содержать только цифры"),
        ("", "Введите 20-значный номер счета"),
    ],
)
def test_get_mask_account(original: str, expected: str) -> None:
    assert get_mask_account(original) == expected
