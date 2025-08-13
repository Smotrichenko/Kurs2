from datetime import datetime
from typing import Optional

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    if not isinstance(card, str) or not card.strip():
        return "Некорректный ввод"

    try:
        if "счет" in card.lower() or "счёт" in card.lower():
            parts = card.split()
            if len(parts) < 2:
                return "Некорректный ввод"
            account_point = card.split()[-1]
            if not account_point.isdigit():
                return "Некорректный номер счета"
            return f"Счет {get_mask_account(account_point)}"
        else:
            parts = card.split()
            if len(parts) < 2:
                return "Некорректный ввод"
            account_card = card.split()[-1]
            if not account_card.isdigit():
                return "Некорректный номер карты"
            name_card = card.split()[:-1]
            name_all = " ".join(name_card)
            name_title = name_all.title()
            return f"{name_title} {get_mask_card_number(account_card)}"
    except Exception as e:
        return f"Ошибка при обработке: {e}"


def get_date(date: Optional[str]) -> str:
    """Функция возвращает дату в формате ДД.ММ.ГГГГ"""
    if not isinstance(date, str) or not date.strip():
        return "Некорректная дата"
    try:
        if date.endswith("Z"):
            date = date[:-1]
        dt = datetime.fromisoformat(date)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        return "Некорректная дата"
