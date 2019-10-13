import requests
import random
import json


class TestApi:

    def post_api(self):
        url = "https://gorest.co.in/public-api/users"
        header = {
                  "Content-Type": "application/json",
                  "Authorization": "Bearer TBi_Y27sxJ9XsBBmRgkb-oXSpjbWUdsotju1",
                  "Accept": "application/json"
        }
        data = {
                "first_name": "Johny Z",
                "last_name": "Rocket",
                "gender": "male",
                "dob": "1970-08-12",
                "email": f'j_z_{str(random.randint(0, 10000))}@mail.kz',
                "phone": "+165776577",
                "website": "https://bit.ly/IqT6zt",
                "address": "Platform 3/4 end of rainbow street",
                "status": "active"
        }

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

    def delete_api(self):
        header = {
                  "Content-Type": "application/json",
                  "Authorization": "Bearer TBi_Y27sxJ9XsBBmRgkb-oXSpjbWUdsotju1",
                  "Accept": "application/json"
        }

        url = f'https://gorest.co.in/public-api/users/{user_id}'
        response = requests.delete(url, headers=header)

        response_code = json.dumps(response.json()['_meta']['code'])
        print(f'\nID #{user_id} DELETE with response {response_code}')

        return response_code
