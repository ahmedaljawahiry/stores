import pytest

from util import get_paginated_response, APP_URL

test_data = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


@pytest.mark.parametrize('page, next_, previous, data', [
    (1, f'{APP_URL}?page=2&', '', test_data[0:3]),
    (2, f'{APP_URL}?page=3&', f'{APP_URL}?page=1&', test_data[3:6]),
    (3, '', f'{APP_URL}?page=2&', test_data[6:9]),
    (10, '', f'{APP_URL}?page=9&', [])
])
def test_paginated_response(page, next_, previous, data):

    response = get_paginated_response(data=test_data, page=page)
    assert response['total'] == len(test_data)
    assert response['page'] == page
    assert response['next'] == next_
    assert response['previous'] == previous
    assert response['data'] == data


def test_extra_query_params_are_passed_to_next_and_previous_urls():

    response = get_paginated_response(
        data=test_data,
        page=2,
        extra_query_params={'dog': 1, 'cat': 2}
    )
    assert response['next'] == f'{APP_URL}?page=3&dog=1&cat=2'
    assert response['previous'] == f'{APP_URL}?page=1&dog=1&cat=2'
