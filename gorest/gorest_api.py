import allure
import requests

import gorest.header_composer as h

base_url = 'https://gorest.co.in/public-api/users/'


class GoRestApi:
    header = h.get_header()

    @allure.step('Create user record - POST')
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

    @allure.step('Change user name - PUT')
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

    @allure.step('Change user email - PATCH')
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

    @allure.step('Get user #{user_id} info - GET')
    def get(self, user_id) -> dict:
        url = f'{base_url}{user_id}'
        response = requests.get(url, headers=self.header)
        assert response.ok

        return response.json()

    @allure.step('Delete user #{user_id} record - DELETE')
    def delete(self, user_id) -> dict:
        url = f'{base_url}{user_id}'
        response = requests.delete(url, headers=self.header)
        assert response.ok

        return response.json()

    @allure.step('Get user #{user_id} name - GET')
    def get_user_name(self, user_id) -> str:
        return self.get(user_id)['data']['name']

    @allure.step('Get user #{user_id} email - GET')
    def get_user_email(self, user_id) -> str:
        return self.get(user_id)['data']['email']
