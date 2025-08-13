from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция принимает список словарей и возвращает новый список словарей,содержащий только те словари,
    у которых ключ state соответствует указанному значению - 'EXECUTED'
    """

    filtered_list_of_dict = []
    for key in data:
        if key.get("state") == state:
            filtered_list_of_dict.append(key)
    return filtered_list_of_dict


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция принимает список словарей и возвращает новый список словарей с сортировкой по убыванию
    по ключу 'data'
    """
    sort_list_of_dict = sorted(data, key=lambda x: x["date"], reverse=reverse)
    return sort_list_of_dict
