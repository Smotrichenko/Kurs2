from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    if "счет" in card.lower():
        account_point = card.split()[-1]
        return f"Счет {get_mask_account(account_point)}"
    else:
        account_card = card.split()[-1]
        name_card = card.split()[:-1]
        name_all = " ".join(name_card)
        name_title = name_all.title()
        return f"{name_title} {get_mask_card_number(account_card)}"


def get_date(date: str) -> str:
    """Функция возвращает дату в формате ДД.ММ.ГГГГ"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
