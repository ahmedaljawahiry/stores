import json

from fastapi import FastAPI

from stores import Stores
from util import get_paginated_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "task": "https://github.com/tailsdotcom/coding-test",
        "role": "full stack engineer",
        "author": "Ahmed Al-Jawahiry",
    }


@app.get("/stores/")
def stores(page: int = 1, search: str = None):
    with open('stores.json') as _json:
        loaded_json = json.load(_json)
        data = Stores(json=loaded_json).filter(search_str=search)
        query_params_to_pass_on = {'search': search} if search else None
        return get_paginated_response(
            data=data,
            page=page,
            extra_query_params=query_params_to_pass_on
        )
