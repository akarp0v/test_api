import pytest

from gorest import GoRestApi, User


@pytest.fixture(scope='session')
def conduct_objects():
    api, user = GoRestApi(), User()

    yield api, user

    del api, user
