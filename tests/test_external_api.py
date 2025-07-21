import json
from unittest.mock import mock_open, patch

from src.external_api import convert_to_rub
from src.utils import get_transaction_amount, load_transactions

# ----------------------
# Тесты для load_transactions
# ----------------------


def test_load_transactions_valid():
    mock_data = [{"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}]
    mock_file_content = json.dumps(mock_data)

    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        result = load_transactions("fake.json")
        assert isinstance(result, list)
        assert result[0]["id"] == 1


def test_load_transactions_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_transactions("fake.json")
        assert result == []


def test_load_transactions_invalid_json():
    with patch("builtins.open", mock_open(read_data="invalid json")):
        with patch("json.load", side_effect=json.JSONDecodeError("error", "doc", 0)):
            result = load_transactions("fake.json")
            assert result == []


def test_load_transactions_not_list():
    mock_file_content = json.dumps({"id": 1})  # JSON-объект вместо списка
    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        result = load_transactions("fake.json")
        assert result == []


# ----------------------
# Тесты для convert_to_rub
# ----------------------


def test_convert_to_rub_rub_currency():
    data = {"amount": "150.5", "currency": {"code": "RUB"}}
    result = convert_to_rub(data)
    assert result == 150.5


@patch("src.utils.requests.get")
def test_convert_to_rub_usd_currency(mock_get):
    mock_response = {"result": 7500.0}
    mock_get.return_value.json.return_value = mock_response

    data = {"amount": "100", "currency": {"code": "USD"}}
    result = convert_to_rub(data)
    assert result == 7500.0


@patch("src.utils.requests.get", side_effect=Exception("API Error"))
def test_convert_to_rub_api_error(_):
    data = {"amount": "100", "currency": {"code": "USD"}}
    result = convert_to_rub(data)
    assert result == 0.0


# ----------------------
# Тесты для get_transaction_amount
# ----------------------


def test_get_transaction_amount_rub():
    tx = {"operationAmount": {"amount": "123.45", "currency": {"code": "RUB"}}}
    result = get_transaction_amount(tx)
    assert result == 123.45


@patch("src.utils.convert_to_rub", return_value=7000.0)
def test_get_transaction_amount_foreign_currency(mock_convert):
    tx = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
    result = get_transaction_amount(tx)
    mock_convert.assert_called_once()
    assert result == 7000.0


def test_get_transaction_amount_missing_key():
    tx = {"id": 1}  # Нет ключа operationAmount
    result = get_transaction_amount(tx)
    assert result == 0.0


def test_get_transaction_amount_invalid_amount():
    tx = {"operationAmount": {"amount": "abc", "currency": {"code": "RUB"}}}
    result = get_transaction_amount(tx)
    assert result == 0.0
