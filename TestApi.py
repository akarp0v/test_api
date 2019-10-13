import requests
import json


class TestApi:

    def post_api(self, data, header):
        url = "https://gorest.co.in/public-api/users"
        response = requests.post(url, headers=header, json=data)

        global user_id
        user_id = json.dumps(response.json()['result']['id']).replace('"', '').rstrip('\n')

        response_code = json.dumps(response.json()['_meta']['code'])
        print(f'\nID #{user_id} POST with response {response_code}')

        return response_code

    def get_api(self):
        cont_type = 'json'
        token = 'TBi_Y27sxJ9XsBBmRgkb-oXSpjbWUdsotju1'
        url = f'https://gorest.co.in/public-api/users/{user_id}?_format={cont_type}&access-token={token}'
        response = requests.get(url)

        response_code = json.dumps(response.json()['_meta']['code'])
        print(f'\nID #{user_id} GET with response {response_code}')

        return response_code

    def delete_api(self, header):
        url = f'https://gorest.co.in/public-api/users/{user_id}'
        response = requests.delete(url, headers=header)

        response_code = json.dumps(response.json()['_meta']['code'])
        print(f'\nID #{user_id} DELETE with response {response_code}')

        return response_code
