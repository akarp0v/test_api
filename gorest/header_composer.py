from .const import TOKEN_PATH


def get_header() -> dict:
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {read_token(TOKEN_PATH)}"
    }


def read_token(path: str) -> str:
    with open(path) as file:
        return file.readline().strip()
