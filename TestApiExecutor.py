import pytest
from TestApi import *


def test_case():
    # execute POST-GET-DELETE-GET test scenario
    test1 = TestApi()
    try:
        print(f'\n-- Test POST-GET-DELETE-GET started --')
        assert test1.post_api() == '200'
        assert test1.get_api() == '200'
        assert test1.delete_api() == '204'
        assert test1.get_api() == '404'
        print(f'\n-- Test POST-GET-DELETE-GET finished --')
    except OSError:
        print(f'\n-- Test POST-GET-DELETE-GET was NOT finished --')
