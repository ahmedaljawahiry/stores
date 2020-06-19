from typing import Iterable, Sized, Union
from urllib.parse import urlencode

PAGE_SIZE = 3
APP_URL = 'http://127.0.0.1:8000/stores/'


def get_paginated_response(data: Union[Iterable, Sized], page: int, extra_query_params: dict = None):
    total_count = len(data)
    slice_from = (page - 1) * PAGE_SIZE
    slice_to = page * PAGE_SIZE
    no_next_page = slice_to > total_count
    url_params = urlencode(extra_query_params) if extra_query_params else ''
    return {
        'total': total_count,
        'page': page,
        'next': '' if no_next_page else f'{APP_URL}?page={page + 1}&{url_params}',
        'previous': f'{APP_URL}?page={page - 1}&{url_params}' if page > 1 else '',
        'data': data[slice_from:slice_to]
    }
