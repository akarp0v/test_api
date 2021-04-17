import base64


def read_token(path: str) -> str:
    with open(path) as file:
        token = file.readline().strip()

        return base64.b64decode(token).decode('utf-8')
