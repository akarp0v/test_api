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
    @staticmethod
    def _perform_request(method: str, user: User) -> requests.Response:
        header = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ.get('TOKEN')}"
        }

        url = os.environ.get('GOREST_URL')
        if method not in (Methods.POST,):
            url += f'{user.id}'

        payload = None
        if method not in (Methods.GET, Methods.DELETE):
            payload = {
                "name": user.name,
                "email": user.email,
                "gender": user.gender,
                "status": user.status
            }

        response = requests.request(method=method, url=url, headers=header, json=payload)
        assert response.ok

        return response

    @allure.step
    def post_request(self, user: User) -> int:
        response = self._perform_request(Methods.POST, user)

        return response.json()['data']['id']

    @allure.step
    def put_request(self, user: User) -> dict:
        response = self._perform_request(Methods.PUT, user)

        return response.json()

    @allure.step
    def patch_request(self, user: User) -> dict:
        response = self._perform_request(Methods.PATCH, user)

        return response.json()

    @allure.step
    def get_request(self, user: User) -> dict:
        response = self._perform_request(Methods.GET, user)

        return response.json()

    @allure.step
    def delete_request(self, user: User) -> dict:
        response = self._perform_request(Methods.DELETE, user)

        return response.json()

    @allure.step
    def get_user_name(self, user: User) -> str:
        return self.get_request(user)['data']['name']

    @allure.step
    def get_user_email(self, user: User) -> str:
        return self.get_request(user)['data']['email']
