token_path = 'gorest/token.txt'


def get_header() -> dict:
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {read_token(token_path)}"
    }


def read_token(path: str) -> str:
    with open(path) as file:
        return file.readline().strip()
