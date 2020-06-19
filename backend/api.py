import json

from fastapi import FastAPI

from stores import Stores
from util import get_paginated_response

app = FastAPI()


@app.get("/")
def home():
    return {
        "task": "https://github.com/tailsdotcom/coding-test",
        "role": "full stack engineer",
        "author": "Ahmed Al-Jawahiry",
    }


@app.get("/stores/")
def stores(page: int = 1):
    with open('stores.json') as _json:
        loaded_json = json.load(_json)
        return get_paginated_response(
            data=Stores(json=loaded_json),
            page=page
        )
