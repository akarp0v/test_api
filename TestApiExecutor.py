import json
from ApiHelper import ApiHelper


def read_file(path):
    with open(path) as file:
        return json.loads(file.read())


def test_1():
    test1 = ApiHelper()
    try:
        print('\n-- Test POST-GET-DELETE-GET started --\n')
        assert test1.post_api(read_file('header.json')) == '200'
        assert test1.get_api() == '200'
        assert test1.delete_api(read_file('header.json')) == '204'
        assert test1.get_api() == '404'
        print('\n-- Test POST-GET-DELETE-GET finished --\n')

    except OSError:
        print('\n-- Test POST-GET-DELETE-GET failed --\n')


def test_2():
    test2 = ApiHelper()
    try:
        print('\n-- Test POST-PUT-GET-DELETE-GET started --\n')
        assert test2.post_api(read_file('header.json')) == '200'
        assert test2.put_api() == '200'
        assert test2.get_api() == '200'
        assert test2.delete_api(read_file('header.json')) == '204'
        assert test2.get_api() == '404'
        print('\n-- Test POST-PUT-GET-DELETE-GET finished --\n')

    except OSError:
        print('\n-- Test POST-PUT-GET-DELETE-GET failed --\n')
