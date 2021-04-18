import allure
import requests
import os

from .user import User


class Methods:
    GET: str = 'GET'
    POST: str = 'POST'
    PUT: str = 'PUT'
    PATCH: str = 'PATCH'
    DELETE: str = 'DELETE'


class GoRestApi:
    def __init__(self, user: User):
        self.user = user
        self.token = os.environ.get('TOKEN')

    def _perform_request(self, method: str) -> requests.Response:
        header = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        url = os.environ.get('GOREST_URL')
        if method != Methods.POST:
            url += f'{self.user.id}'

        payload = None
        if method not in (Methods.GET, Methods.DELETE):
            payload = {
                "name": self.user.name,
                "email": self.user.email,
                "gender": self.user.gender,
                "status": self.user.status
            }

        response = requests.request(method=method, url=url, headers=header, json=payload)
        assert response.ok, response.content.decode()

        return response

    @allure.step
    def post_user(self) -> requests.Response:
        response = self._perform_request(Methods.POST)

        return response

    @allure.step
    def put_user(self) -> requests.Response:
        response = self._perform_request(Methods.PUT)

        return response

    @allure.step
    def patch_user(self) -> requests.Response:
        response = self._perform_request(Methods.PATCH)

        return response

    @allure.step
    def get_user(self) -> requests.Response:
        response = self._perform_request(Methods.GET)

        return response

    @allure.step
    def delete_user(self) -> requests.Response:
        response = self._perform_request(Methods.DELETE)

        return response
