def get_mask_card_number(number_card: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    part_1 = number_card[:4]
    part_2 = number_card[4:6]
    mask_card = "** ****"
    part_3 = number_card[-4:]
    return f"{part_1} {part_2}{mask_card} {part_3}"


number_card = input("Введите номер карты: ")
print(get_mask_card_number(number_card))


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    return f"**{account_number[-4:]}"


account_number = input("Введите номер счета: ")
print(get_mask_account(account_number))
