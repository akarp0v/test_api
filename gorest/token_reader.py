import base64

from .const import TOKEN_PATH


def read_token(path: str = TOKEN_PATH) -> str:
    with open(path) as file:
        token = file.readline().strip()

        return base64.b64decode(token).decode('utf-8')
