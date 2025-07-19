import pytest

from src.decorators import log

from tests.conftest import temp_log_file


def test_log_success_console(capsys):
    @log()
    def add(x, y):
        return x + y

    result = add(3, 4)
    captured = capsys.readouterr()

    assert result == 7
    assert "Начало выполнения функции add" in captured.out
    assert "Окончание выполнения функции add" in captured.out
    assert "Результат: 7" in captured.out


def test_log_success_file(temp_log_file):
    @log(filename=temp_log_file)
    def multiply(x, y):
        return x * y

    result = multiply(2, 5)
    assert result == 10

    # Проверяем, что файл создан и содержит нужные строки
    with open(temp_log_file, encoding="utf-8") as f:
        content = f.read()

    assert "Начало выполнения функции multiply" in content
    assert "Окончание выполнения функции multiply" in content
    assert "Результат: 10" in content


def test_log_exception_file(temp_log_file):
    @log(filename=temp_log_file)
    def fail_func():
        raise RuntimeError("Something went wrong")

    with pytest.raises(RuntimeError, match="Something went wrong"):
        fail_func()

    with open(temp_log_file, encoding="utf-8") as f:
        content = f.read()

    assert "Начало выполнения функции fail_func" in content
    assert "Ошибка в функции fail_func" in content
    assert "Ошибка Something went wrong" in content
