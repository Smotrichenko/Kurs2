from unittest.mock import Mock, patch

from src.external_api import convert_to_rub
from src.utils import get_transaction_amount


# ----- ТЕСТЫ ДЛЯ convert_to_rub -----
@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get):
    # Мокаем ответ API
    mock_response = Mock()
    mock_response.json.return_value = {"result": 100.0}
    mock_get.return_value = mock_response

    result = convert_to_rub(1, "USD")
    assert result == 100.0
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_convert_to_rub_api_error(mock_get):
    # Если API возвращает некорректный ответ
    mock_response = Mock()
    mock_response.json.return_value = {}
    mock_get.return_value = mock_response

    result = convert_to_rub(10, "EUR")
    assert result == 0.0  # ожидаем 0.0 по умолчанию


# ----- ТЕСТЫ ДЛЯ get_transaction_amount -----
def test_get_transaction_amount_rub():
    transaction = {"operationAmount": {"amount": "5000", "currency": {"code": "RUB"}}}
    result = get_transaction_amount(transaction)
    assert result == 5000.0


@patch("src.external_api.convert_to_rub")
def test_get_transaction_amount_usd(mock_convert):
    mock_convert.return_value = 9000.0
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

    result = get_transaction_amount(transaction)
    assert result == 9000.0
    mock_convert.assert_called_once_with(100.0, "USD")


def test_get_transaction_amount_missing_operation_amount():
    transaction = {}
    result = get_transaction_amount(transaction)
    assert result == 0.0
