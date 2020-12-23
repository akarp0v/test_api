from gorest import GoRestApi
from gorest import User

api = GoRestApi()
user = User.info()
test_name = "Put Request"
test_email = "patch@request.api"


def test_post_request():
    user.id = api.post(user)

    assert api.get_user_email(user.id) == user.email, "POST test FAILED"


def test_put_request():
    assert api.get_user_name(user.id) != test_name
    user.name = test_name
    api.put(user)

    assert api.get_user_name(user.id) == test_name, "PUT test FAILED"


def test_patch_request():
    assert api.get_user_email(user.id) != test_email
    user.email = test_email
    api.patch(user)

    assert api.get_user_email(user.id) == test_email, "PATCH test FAILED"


def test_delete_request():
    api.delete(user.id)

    assert api.get(user.id)['code'] == 404, "DELETE test FAILED"
