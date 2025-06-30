import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("2200701052954101") == "2200 70** **** 4101"

    assert get_mask_card_number("220070105295410") == "Недостаточная длина номера карты"

    assert get_mask_card_number("22007010529541012") == "Слишком длинный номер карты"

    assert get_mask_card_number("2200701oo2954101") == "Номер счета должен содержать только цифры"

    assert get_mask_card_number("") == "Введите номер карты"


def test_get_mask_accaunt():
    assert get_mask_account("40817810900111108057") == "**8057"

    assert get_mask_account("4081781090011110805") == "Введите 20-значный номер счета"

    assert get_mask_account("408178109001111080570") == "Введите 20-значный номер счета"

    assert get_mask_account("4081781090011ll08057") == "Номер счета должен содержать только цифры"

    assert get_mask_account("") == "Введите 20-значный номер счета"
