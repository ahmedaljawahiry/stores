from typing import Iterable, Sized, Union

PAGE_SIZE = 3
APP_URL = 'http://127.0.0.1:8000/stores/'


def get_paginated_response(data: Union[Iterable, Sized], page: int):
    total_count = len(data)
    slice_from = (page - 1) * PAGE_SIZE
    slice_to = page * PAGE_SIZE
    no_next_page = slice_to > total_count
    return {
        'total': total_count,
        'page': page,
        'next': '' if no_next_page else f'{APP_URL}?page={page + 1}',
        'previous': f'{APP_URL}?page={page - 1}' if page > 1 else '',
        'data': data[slice_from:slice_to]
    }
