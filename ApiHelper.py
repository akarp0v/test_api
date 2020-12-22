import requests
from users import User


def read_token(path):
    with open(path) as file:
        return file.readline().strip()


def get_header():
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {read_token('token.txt')}"
    }


class ApiHelper:
    user = User()

    def post_api(self):
        url = "https://gorest.co.in/public-api/users"
        req_data = self.user.info()
        response = requests.post(url, headers=get_header(), json=req_data)
        self.user.id = response.json()['data']['id']

        return response.json()['code']

    def put_api(self):
        url = f'https://gorest.co.in/public-api/users/{self.user.id}'
        req_data = self.user.info()
        response = requests.put(url, headers=get_header(), json=req_data)

        return response.json()['code']

    def get_api(self):
        url = f'https://gorest.co.in/public-api/users/{self.user.id}'
        response = requests.get(url, headers=get_header())

        return response.json()['code']

    def delete_api(self):
        url = f'https://gorest.co.in/public-api/users/{self.user.id}'
        response = requests.delete(url, headers=get_header())

        return response.json()['code']
