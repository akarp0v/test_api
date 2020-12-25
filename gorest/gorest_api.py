import allure
import requests

import gorest.header_composer as h

base_url = 'https://gorest.co.in/public-api/users/'


class GoRestApi:
    header = h.get_header()

    @allure.step
    def post_request(self, user) -> int:
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

    @allure.step
    def put_request(self, user) -> dict:
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

    @allure.step
    def patch_request(self, user) -> dict:
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

    @allure.step
    def get_request(self, user_id) -> dict:
        url = f'{base_url}{user_id}'
        response = requests.get(url, headers=self.header)
        assert response.ok

        return response.json()

    @allure.step
    def delete_request(self, user_id) -> dict:
        url = f'{base_url}{user_id}'
        response = requests.delete(url, headers=self.header)
        assert response.ok

        return response.json()

    @allure.step
    def get_user_name(self, user_id) -> str:
        return self.get_request(user_id)['data']['name']

    @allure.step
    def get_user_email(self, user_id) -> str:
        return self.get_request(user_id)['data']['email']
