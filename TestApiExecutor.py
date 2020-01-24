import pytest
import json
from ApiHelper import *


def read_file(path):
    with open(path, 'r') as file:
        return json.loads(file.read())


def test_case():
    test1 = ApiHelper()
    try:
        print(f'\n-- Test POST-GET-DELETE-GET started --')
        assert test1.post_api(read_file('header.json')) == '200'
        assert test1.get_api() == '200'
        assert test1.delete_api(read_file('header.json')) == '204'
        assert test1.get_api() == '404'

        print(f'\n-- Test POST-GET-DELETE-GET finished --')
    except OSError:
        print(f'\n-- Test POST-GET-DELETE-GET was NOT finished --')
