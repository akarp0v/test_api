from pytest import fixture

from gorest import GoRestApi, User


@fixture(scope='session')
def api():
    user = User()
    api = GoRestApi(user)

    yield api, user

    del user, api
