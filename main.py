import re
import os
from typing import List, Dict
from src.utils import load_transactions, get_transaction_amount
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.widget import mask_account_card, get_date
from src.external_api import convert_to_rub


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [tx for tx in data if pattern.search(tx.get("description", " "))]


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    stats = {cat: 0 for cat in categories}
    for tx in data:
        for cat in categories:
            if cat.lower() in tx.get("description", " ").lower:
                stats[cat] += 1
    return stats
