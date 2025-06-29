def get_mask_card_number(number_card: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if not isinstance(number_card, str) or len(number_card) == 0:
        return "Введите номер карты"
    if not number_card.isdigit():
        return "Номер счета должен содержать только цифры"
    if len(number_card) < 16:
        return "Недостаточная длина номера карты"
    if len(number_card) > 16:
        return "Слишком длинный номер карты"

    part_1 = number_card[:4]
    part_2 = number_card[4:6]
    mask_card = "** ****"
    part_3 = number_card[-4:]
    return f"{part_1} {part_2}{mask_card} {part_3}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if len(account_number) != 20:
        return "Введите 20-значный номер счета"
    if not account_number.isdigit():
        return "Номер счета должен содержать только цифры"
    return f"**{account_number[-4:]}"
