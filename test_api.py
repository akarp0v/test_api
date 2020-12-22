from gorest import GoRestApi


def test_post_get_delete():
    api = GoRestApi()
    assert api.post_api() == 201
    assert api.get_api() == 200
    assert api.delete_api() == 204

    assert api.get_api() == 404


def test_post_put_get_delete():
    api = GoRestApi()
    assert api.post_api() == 201
    assert api.put_api() == 200
    assert api.get_api() == 200
    assert api.delete_api() == 204

    assert api.get_api() == 404
