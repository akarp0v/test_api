from .const import GorestConst

gc = GorestConst()


def get_header() -> dict:
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {read_token()}"
    }


def read_token(path: str = gc.TOKEN_PATH) -> str:
    with open(path) as file:
        return file.readline().strip()
