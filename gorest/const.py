import os


class GorestConst:
    GOREST_URL = os.environ.get('GOREST_URL', 'https://gorest.co.in/public-api/users/')

    TOKEN_PATH = 'gorest/token.txt'

    TEST_NAME = "Put Request"
    TEST_EMAIL = "patch@request.api"
