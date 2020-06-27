import json

import pytest
from fastapi.testclient import TestClient

from api import app


@pytest.fixture(scope='session')
def client():
    return TestClient(app)


@pytest.fixture(scope='session')
def store_json():
    file = open('stores.json')
    yield json.load(file)
    file.close()


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "author": "Ahmed Al-Jawahiry",
    }


def test_stores_api_with_no_page(client, store_json):
    response = client.get("/stores/")
    assert response.status_code == 200
    assert response.json()['data'] == store_json[0:3]


def test_stores_api_with_page(client, store_json):
    response = client.get("/stores/?page=4")
    assert response.status_code == 200
    assert response.json()['data'] == store_json[9:12]


def test_can_search(client, store_json):
    response = client.get("/stores/?search=st_alb")
    assert response.status_code == 200

    response_json = response.json()
    assert response_json['data'] == [{"name": "St_Albans", "postcode": "AL1 2RJ"}]
    assert response_json['total'] == 1
    assert not response_json['next']
