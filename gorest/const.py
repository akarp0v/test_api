from essential_generators import DocumentGenerator as Gen
import os

from .reader import read_token


GOREST_URL = os.environ.setdefault('GOREST_URL', 'https://gorest.co.in/public-api/users/')
TOKEN = os.environ.setdefault('TOKEN', read_token('gorest/data/token.txt'))

TEST_NAME = f'test-{Gen().name()}'
TEST_EMAIL = f'test-{Gen().email()}'
