import requests

from gorest.users import User
import gorest.helper as h

base_url = 'https://gorest.co.in/public-api/users/'


class GoRestApi:
    user = User()

    def post_api(self) -> int:
        url = base_url
        response = requests.post(url, headers=h.get_header(), json=self.user.info())
        self.user.id = response.json()['data']['id']

        return response.json()['code']

    def put_api(self) -> int:
        url = f'{base_url}{self.user.id}'
        response = requests.put(url, headers=h.get_header(), json=self.user.info())

        return response.json()['code']

    def get_api(self) -> int:
        url = f'{base_url}{self.user.id}'
        response = requests.get(url, headers=h.get_header())

        return response.json()['code']

    def delete_api(self) -> int:
        url = f'{base_url}{self.user.id}'
        response = requests.delete(url, headers=h.get_header())

        return response.json()['code']
