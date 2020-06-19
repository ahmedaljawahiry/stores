from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Store:
    name: str
    postcode: str


class Stores:

    POST_CODE = "postcode"
    NAME = "name"

    def __init__(self, json: List[Dict[str, str]]):
        self._stores = [Store(**store_dict) for store_dict in json]

    def __getitem__(self, item):
        return self._stores[item]

    def __len__(self):
        return len(self._stores)

    def filter(self, search_str: str):
        postcode_matches = []
        name_matches = []
        lowercase_search_str = search_str.lower()
        for store in self:
            if lowercase_search_str in store.postcode.lower():
                postcode_matches.append(store)
            elif lowercase_search_str in store.name.lower():
                name_matches.append(store)
        return postcode_matches + name_matches
