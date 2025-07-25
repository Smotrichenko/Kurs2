import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

log_file_path = os.path.join(LOG_DIR, "masks.log")
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file_path, mode='w', encoding="utf=8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if not isinstance(number_card, str) or len(number_card) == 0:
        logger.error('Введен неправильный номер карты')
        return "Введите номер карты"
    elif not number_card.isdigit():
        logger.error('Введен неправильный номер карты')
        return "Номер счета должен содержать только цифры"
    elif len(number_card) < 16:
        logger.error('Введен неправильный номер карты')
        return "Недостаточная длина номера карты"
    elif len(number_card) > 16:
        logger.error('Введен неправильный номер карты')
        return "Слишком длинный номер карты"
    else:
        part_1 = number_card[:4]
        part_2 = number_card[4:6]
        mask_card = "** ****"
        part_3 = number_card[-4:]
        logger.debug('Выполнено успешное маскирование карты')
        return f"{part_1} {part_2}{mask_card} {part_3}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if len(account_number) != 20:
        logger.error('Введен неправильный номер счета')
        return "Введите 20-значный номер счета"
    elif not account_number.isdigit():
        logger.error('Введен неправильный номер счета')
        return "Номер счета должен содержать только цифры"
    else:
        logger.debug('Выполнено успешное маскирование счета')
        return f"**{account_number[-4:]}"
