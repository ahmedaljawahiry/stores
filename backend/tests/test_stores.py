import pytest

from stores import Stores, Store


@pytest.fixture(scope='module')
def stores():
    return Stores(json=[
        {"name": "Orpington", "postcode": "BR5 3RP"},
        {"name": "Bracknell", "postcode": "RG12 1EN"},
        {"name": "Broadstairs", "postcode": "CT10 2RQ"},
        {"name": "Tunbridge_Wells", "postcode": "TN2 3FB"},
        {"name": "Brentford", "postcode": "TW8 8JW"},
    ])


def test_can_create():
    stores_json = [
        {"name": "St_Albans", "postcode": "AL1 2RJ"},
        {"name": "Hatfield", "postcode": "AL9 5JP"},
        {"name": "Worthing", "postcode": "BN14 9GB"}
    ]

    stores = Stores(json=stores_json)
    assert len(stores) == len(stores_json)
    for json in stores_json:
        assert Store(**json) in stores


@pytest.mark.parametrize('search_str, expected_result', [
    ('Orp', ['Orpington']),
    ('ORP', ['Orpington']),  # case insensitive
    ('or', ['Orpington', 'Brentford']),
    ('br', ['Orpington', 'Bracknell', 'Broadstairs', 'Tunbridge_Wells', 'Brentford']),  # postcode matches first
    ('nomatch', []),
    ('', ['Orpington', 'Bracknell', 'Broadstairs', 'Tunbridge_Wells', 'Brentford'])
])
def test_can_search(stores, search_str, expected_result):
    results = stores.filter(search_str=search_str)
    assert [s.name for s in results] == expected_result
