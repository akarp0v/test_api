import allure
import requests

import gorest.header_composer as h
from .const import GorestConst
from .user_generator import User

gc = GorestConst()


class GoRestApi:
    header = h.get_header()

    @allure.step
    def post_request(self, user: User) -> int:
        url = gc.GOREST_URL
        payload = {
            "name": user.name,
            "email": user.email,
            "gender": user.gender,
            "status": user.status
        }
        response = requests.post(url, headers=self.header, json=payload)
        assert response.ok

        return response.json()['data']['id']

    @allure.step
    def put_request(self, user: User) -> dict:
        url = f'{gc.GOREST_URL}{user.id}'
        payload = {
            "name": user.name,
            "email": user.email,
            "gender": user.gender,
            "status": user.status
        }
        response = requests.put(url, headers=self.header, json=payload)
        assert response.ok

        return response.json()

    @allure.step
    def patch_request(self, user: User) -> dict:
        url = f'{gc.GOREST_URL}{user.id}'
        payload = {
            "name": user.name,
            "email": user.email,
            "gender": user.gender,
            "status": user.status
        }
        response = requests.patch(url, headers=self.header, json=payload)
        assert response.ok

        return response.json()

    @allure.step
    def get_request(self, user_id: int) -> dict:
        url = f'{gc.GOREST_URL}{user_id}'
        response = requests.get(url, headers=self.header)
        assert response.ok

        return response.json()

    @allure.step
    def delete_request(self, user_id: int) -> dict:
        url = f'{gc.GOREST_URL}{user_id}'
        response = requests.delete(url, headers=self.header)
        assert response.ok

        return response.json()

    @allure.step
    def get_user_name(self, user_id: int) -> str:
        return self.get_request(user_id)['data']['name']

    @allure.step
    def get_user_email(self, user_id: int) -> str:
        return self.get_request(user_id)['data']['email']
