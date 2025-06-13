from src.masks.main import get_mask_card_number, get_mask_account

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




cards = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305"
]

for card in cards:
    print(mask_account_card(card))