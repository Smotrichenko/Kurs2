import datetime
from functools import wraps


def log(filename=None):
    """
    Декоратор, который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message_start = f"Начало выполнения функции {func.__name__}:{start_time}\n"

            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(message_start)
            else:
                print(message_start)

            try:
                result = func(*args, **kwargs)
                end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                message_end = f"Окончание выполнения функции {func.__name__}:{end_time}\n" f"Результат: {result}\n"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message_end)
                        f.write("-" * 52 + "\n")
                else:
                    print(message_end)

                return result

            except Exception as e:
                error_message = (
                    f"Ошибка в функции {func.__name__} при вызове с аргументами: {args}, {kwargs}.\n" f"Ошибка {e}\n"
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message)
                        f.write("-" * 52 + "\n")
                else:
                    print(error_message)

                raise

        return wrapper

    return decorator
