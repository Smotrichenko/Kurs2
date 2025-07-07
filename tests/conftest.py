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
