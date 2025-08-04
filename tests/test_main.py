from main import process_bank_search, process_bank_operations


def test_process_bank_search_exact_match(sample_data):
    result = process_bank_search(sample_data, "перевод")
    assert len(result) == 1
    assert result[0]["description"] == "Перевод организации"

def test_process_bank_search_case_insensitive(sample_data):
    result = process_bank_search(sample_data, "опЛАтА")
    assert len(result) == 1
    assert result[0]["description"] == "Оплата услуг"

def test_process_bank_search_no_match(sample_data):
    result = process_bank_search(sample_data, "кредит")
    assert result == []


def test_process_bank_operations_basic():
    data = [
        {"description": "Пополнение счета"},
        {"description": "Оплата услуг"},
        {"description": "Оплата услуг"},
        {"description": "Перевод организации"},
    ]
    categories = ["Пополнение", "Оплата", "Перевод"]
    result = process_bank_operations(data, categories)

    assert result == {"Пополнение": 1, "Оплата": 2, "Перевод": 1}


def test_process_bank_operations_no_match():
    data = [{"description": "Неизвестная операция"}]
    categories = ["Кредит", "Снятие"]
    result = process_bank_operations(data, categories)

    assert result == {"Кредит": 0, "Снятие": 0}
