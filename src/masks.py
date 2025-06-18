def get_mask_card_number(number_card: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    part_1 = number_card[:4]
    part_2 = number_card[4:6]
    mask_card = "** ****"
    part_3 = number_card[-4:]
    return f"{part_1} {part_2}{mask_card} {part_3}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    return f"**{account_number[-4:]}"
