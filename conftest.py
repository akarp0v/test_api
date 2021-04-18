import pytest

from gorest import GoRestApi, User


@pytest.fixture(scope='session')
def conduct_api():
    user = User()
    api = GoRestApi(user)

    yield api, user

    del user, api
