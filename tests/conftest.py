from typing import Any, Dict, List

import pytest


@pytest.fixture
def filt_list() -> List[Dict[str, Any]]:
    """Фикстура с тестовыми данными"""
    return [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "EXECUTED"},
        {"id": 3, "state": "CANCELLED"},
        {"id": 4, "name": "None"},
    ]


@pytest.fixture
def sort_date() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "date": "2024-05-01"},
        {"id": 2, "date": "2024-01-15"},
        {"id": 3, "date": "2024-03-20"},
        {"id": 4, "date": "2024-05-01"},
        {"id": 5, "date": "None"},
    ]


@pytest.fixture
def transactions():
    return [
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
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]


@pytest.fixture
def temp_log_file(tmp_path):
    path = tmp_path / "test_log.txt"
    yield str(path)
    if path.exists():
        path.unlink()
