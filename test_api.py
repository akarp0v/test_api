import allure

from gorest import GoRestApi
from gorest import User

api = GoRestApi()
user = User.info()
test_name = "Put Request"
test_email = "patch@request.api"


@allure.description("""
<h2 style="color: #97cd64;">Create user record - POST</h2>
<h4 style="color: #999999;">https://gorest.co.in</h4>
1. Create new user<br>
2. POST user state to API<br>
3. GET user email from API<br>
4. Compare initial user emails with API email &rarr; expect True
""")
@allure.step('POST step')
def test_post_request():
    user.id = api.post(user)

    with allure.step('Compare initial email with API user email'):
        assert api.get_user_email(user.id) == user.email, "POST test FAILED"


@allure.description("""
<h2 style="color: #97cd64;">Change user name - PUT</h2>
<h4 style="color: #999999;">https://gorest.co.in</h4>
1. Compare API user name with test name &rarr; expect False<br>
2. Change initial user name to test name<br>
3. Send changed user state to API<br>
4. Compare test name with API user name &rarr; expect True
""")
@allure.step('PUT step')
def test_put_request():
    with allure.step('Compare API user name and test name'):
        assert api.get_user_name(user.id) != test_name
    with allure.step('Change initial user name to test name'):
        user.name = test_name
    api.put(user)

    with allure.step('Compare test name and API user name'):
        assert api.get_user_name(user.id) == test_name, "PUT test FAILED"


@allure.description("""
<h2 style="color: #97cd64;">Change user email - PATCH</h2>
<h4 style="color: #999999;">https://gorest.co.in</h4>
1. Compare API user email with test email &rarr; expect False<br>
2. Change initial user email to test email<br>
3. Send changed user state to API<br>
4. Compare test email with API user email &rarr; expect True
""")
@allure.step('PATCH step')
def test_patch_request():
    with allure.step('Compare API user email with test email'):
        assert api.get_user_email(user.id) != test_email
    with allure.step('Change initial user email to test email'):
        user.email = test_email
    api.patch(user)

    with allure.step('Compare test email with API user email'):
        assert api.get_user_email(user.id) == test_email, "PATCH test FAILED"


@allure.description("""
<h2 style="color: #97cd64;">Remove user record - DELETE</h2>
<h4 style="color: #999999;">https://gorest.co.in</h4>
1. Delete API user record<br>
2. Check is API user deleted &rarr; expect True
""")
@allure.step('DELETE step')
def test_delete_request():
    api.delete(user.id)

    with allure.step('Check is API user deleted'):
        assert api.get(user.id)['code'] == 404, "DELETE test FAILED"
