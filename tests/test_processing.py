from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "data, state, expected",
    [
        (
            [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "PENDING"}, {"id": 3, "state": "EXECUTED"}],
            "EXECUTED",
            [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}],
        ),
        (
            [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "CANCELED"}, {"id": 3, "state": "EXECUTED"}],
            "CANCELED",
            [{"id": 2, "state": "CANCELED"}],
        ),
        ([{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "EXECUTED"}], "CANCELLED", []),
        ([], "EXECUTED", []),
        (
            [
                {"id": 1, "name": "Test"},
                {"id": 2, "state": "EXECUTED"},
            ],
            "EXECUTED",
            [
                {"id": 2, "state": "EXECUTED"},
            ],
        ),
    ],
)
def test_filter_by_state(data: List[Dict[str, Any]], state: str, expected: List[Dict[str, Any]]):
    assert filter_by_state(data, state) == expected

    def test_filter_executed(filter_list):
        result = filter_by_state(filter_list, state="EXECUTED")
        expected = [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "EXECUTED"},
        ]
        assert result == expected

    def test_filter_cancelled(filt_list):
        result = filter_by_state(filt_list, state="CANCELLED")
        expected = [
            {"id": 3, "state": "CANCELLED"},
        ]
        assert result == expected

    def test_filter_no_matches(filt_list):
        result = filter_by_state(filt_list, state="None")
        expected = []
        assert result == expected

    def test_filter_empty_data():
        result = filter_by_state([], state="EXECUTED")
        expected = []
        assert result == expected


def test_sort_descending(sort_date):
    sorted_data = sort_by_date(sort_date, reverse=True)
    dates = [item.get("date", "") for item in sorted_data]
    assert dates == [
        "None",
        "2024-05-01",
        "2024-05-01",
        "2024-03-20",
        "2024-01-15",
    ]


def test_sort_ascending(sort_date):
    sorted_data = sort_by_date(sort_date, reverse=False)
    dates = [item.get("date", "") for item in sorted_data]
    assert dates == [
        "2024-01-15",
        "2024-03-20",
        "2024-05-01",
        "2024-05-01",
        "None",
    ]


def test_empty_list():
    result = sort_by_date([])
    assert result == []
