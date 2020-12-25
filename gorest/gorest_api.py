import allure
import requests

import gorest.header_composer as h

base_url = 'https://gorest.co.in/public-api/users/'


class GoRestApi:
    header = h.get_header()

    @allure.step('POST - create API user record')
    def post(self, user) -> int:
        url = base_url
        req_data = {
            "name": user.name,
            "email": user.email,
            "gender": user.gender,
            "status": user.status
        }
        response = requests.post(url, headers=self.header, json=req_data)
        assert response.ok

        return response.json()['data']['id']

    @allure.step('PUT - change API user name')
    def put(self, user) -> dict:
        url = f'{base_url}{user.id}'
        req_data = {
            "name": user.name,
            "email": user.email,
            "gender": user.gender,
            "status": user.status
        }
        response = requests.put(url, headers=self.header, json=req_data)
        assert response.ok

        return response.json()

    @allure.step('PATCH - change API user email')
    def patch(self, user) -> dict:
        url = f'{base_url}{user.id}'
        req_data = {
            "name": user.name,
            "email": user.email,
            "gender": user.gender,
            "status": user.status
        }
        response = requests.patch(url, headers=self.header, json=req_data)
        assert response.ok

        return response.json()

    @allure.step('GET - get API user #{user_id} state')
    def get(self, user_id) -> dict:
        url = f'{base_url}{user_id}'
        response = requests.get(url, headers=self.header)
        assert response.ok

        return response.json()

    @allure.step('DELETE - remove API user #{user_id} record')
    def delete(self, user_id) -> dict:
        url = f'{base_url}{user_id}'
        response = requests.delete(url, headers=self.header)
        assert response.ok

        return response.json()

    @allure.step('GET - get API user #{user_id} name')
    def get_user_name(self, user_id) -> str:
        return self.get(user_id)['data']['name']

    @allure.step('GET - get API user #{user_id} email')
    def get_user_email(self, user_id) -> str:
        return self.get(user_id)['data']['email']
