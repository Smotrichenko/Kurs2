from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция принимает список словарей и возвращает новый список словарей,содержащий только те словари,
    у которых ключ state соответствует указанному значению - 'EXECUTED'"""

    filtered_list_of_dict = []
    for key in data:
        if key.get("state") == state:
            filtered_list_of_dict.append(key)
        else:
            continue
    return filtered_list_of_dict


data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
result = filter_by_state(data)
print(result)
