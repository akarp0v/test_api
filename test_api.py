import allure

from gorest import TEST_NAME, TEST_EMAIL


@allure.description("""
<h2 style="color: #97cd64;">POST user record</h2>
<h4 style="color: #999999;">https://gorest.co.in</h4>
1. POST local user to API<br>
2. Compare local user email with API email &rarr; expect True
""")
@allure.step('POST step')
def test_post_request(conduct_objects):
    with allure.step('POST local user to API'):
        api, user = conduct_objects
        user.id = api.post_request(user)

    with allure.step('Compare local user email with API email'):
        assert api.get_user_email(user) == user.email, "POST test FAILED"


@allure.description("""
<h2 style="color: #97cd64;">PUT user name</h2>
<h4 style="color: #999999;">https://gorest.co.in</h4>
1. Compare API user name with test name &rarr; expect False<br>
2. Change local user name to test name<br>
3. Send changed user state to API<br>
4. Compare test name with API user name &rarr; expect True
""")
@allure.step('PUT step')
def test_put_request(conduct_objects):
    with allure.step('Compare API user name and test name'):
        api, user = conduct_objects
        assert api.get_user_name(user) != TEST_NAME
    with allure.step('Change local user name to test name'):
        user.name = TEST_NAME
    with allure.step('Send changed user state to API'):
        api.put_request(user)

    with allure.step('Compare test name and API user name'):
        assert api.get_user_name(user) == TEST_NAME, "PUT test FAILED"


@allure.description("""
<h2 style="color: #97cd64;">PATCH user email</h2>
<h4 style="color: #999999;">https://gorest.co.in</h4>
1. Compare API user email with test email &rarr; expect False<br>
2. Change local user email to test email<br>
3. Send changed user state to API<br>
4. Compare test email with API user email &rarr; expect True
""")
@allure.step('PATCH step')
def test_patch_request(conduct_objects):
    with allure.step('Compare API user email with test email'):
        api, user = conduct_objects
        assert api.get_user_email(user) != TEST_EMAIL
    with allure.step('Change local user email to test email'):
        user.email = TEST_EMAIL
    with allure.step('Send changed user state to API'):
        api.patch_request(user)

    with allure.step('Compare test email with API user email'):
        assert api.get_user_email(user) == TEST_EMAIL, "PATCH test FAILED"


@allure.description("""
<h2 style="color: #97cd64;">DELETE user record</h2>
<h4 style="color: #999999;">https://gorest.co.in</h4>
1. Delete user record<br>
2. Check is user deleted &rarr; expect True
""")
@allure.step('DELETE step')
def test_delete_request(conduct_objects):
    with allure.step('Delete user record'):
        api, user = conduct_objects
        api.delete_request(user)

    with allure.step('Check is user deleted'):
        assert api.get_request(user)['code'] == 404, "DELETE test FAILED"
