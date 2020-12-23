import requests

import gorest.header_composer as h

base_url = 'https://gorest.co.in/public-api/users/'


class GoRestApi:
    header = h.get_header()

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

    def get(self, user_id) -> dict:
        url = f'{base_url}{user_id}'
        response = requests.get(url, headers=self.header)
        assert response.ok

        return response.json()

    def delete(self, user_id) -> dict:
        url = f'{base_url}{user_id}'
        response = requests.delete(url, headers=self.header)
        assert response.ok

        return response.json()

    def get_user_name(self, user_id) -> str:
        return self.get(user_id)['data']['name']

    def get_user_email(self, user_id) -> str:
        return self.get(user_id)['data']['email']


