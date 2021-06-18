import allure

from gorest import TEST_NAME, TEST_EMAIL


@allure.description("""
<h2 style="color: #97cd64;">POST user record</h2>
<h4 style="color: #999999;">https://gorest.co.in</h4>
1. POST local user to API<br>
2. Compare local user email with API email &rarr; expect True
""")
def test_post_request(api):
    with allure.step('POST local user to remote API'):
        api, user = api
        response = api.post_user()
        user.id = response.json()['data']['id']
    with allure.step('Try to get user record'):
        response = api.get_user()
    with allure.step('Compare local user email with API email'):
        assert response.json()['data']['email'] == user.email, "POST test FAILED"


@allure.description("""
<h2 style="color: #97cd64;">PUT user name</h2>
<h4 style="color: #999999;">https://gorest.co.in</h4>
1. Compare API user name with test name &rarr; expect False<br>
2. Change local user name to test name<br>
3. Send changed user state to API<br>
4. Compare test name with API user name &rarr; expect True
""")
def test_put_request(api):
    with allure.step('Compare user name and test name'):
        api, user = api
        assert user.name != TEST_NAME
    with allure.step('Change local user name to test name'):
        user.name = TEST_NAME
    with allure.step('Send changed user state to API'):
        api.put_user()
    with allure.step('Try to get user record'):
        response = api.get_user()
    with allure.step('Compare test name and API user name'):
        assert response.json()['data']['name'] == TEST_NAME, "PUT test FAILED"


@allure.description("""
<h2 style="color: #97cd64;">PATCH user email</h2>
<h4 style="color: #999999;">https://gorest.co.in</h4>
1. Compare API user email with test email &rarr; expect False<br>
2. Change local user email to test email<br>
3. Send changed user state to API<br>
4. Compare test email with API user email &rarr; expect True
""")
def test_patch_request(api):
    with allure.step('Compare user email with test email'):
        api, user = api
        assert user.email != TEST_EMAIL
    with allure.step('Change local user email to test email'):
        user.email = TEST_EMAIL
    with allure.step('Send changed user state to API'):
        api.patch_user()
    with allure.step('Try to get user record'):
        response = api.get_user()
    with allure.step('Compare test email with API user email'):
        assert response.json()['data']['email'] == TEST_EMAIL, "PATCH test FAILED"


@allure.description("""
<h2 style="color: #97cd64;">DELETE user record</h2>
<h4 style="color: #999999;">https://gorest.co.in</h4>
1. Delete user record<br>
2. Check is user deleted &rarr; expect True
""")
def test_delete_request(api):
    with allure.step('Delete user record'):
        api, user = api
        response = api.delete_user()
        assert response.json()['code'] == 204
    with allure.step('Try to get user record'):
        response = api.get_user()
    with allure.step('Verify is user deleted'):
        assert response.json()['code'] == 404, "DELETE test FAILED"
