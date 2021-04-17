from essential_generators import DocumentGenerator as Gen
import os


GOREST_URL = os.environ.get('GOREST_URL', 'https://gorest.co.in/public-api/users/')

TOKEN_PATH = 'gorest/data/token.txt'

TEST_NAME = f'test-{Gen().name()}'
TEST_EMAIL = f'test-{Gen().email()}'
