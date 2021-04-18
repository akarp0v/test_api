import pytest

from gorest import GoRestApi, User


@pytest.fixture(scope='session')
def gorest_api():
    user = User()
    api = GoRestApi(user)

    yield api

    del api, user
