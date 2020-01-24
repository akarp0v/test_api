import requests
import json
from essential_generators import DocumentGenerator


class ApiHelper:
    user_id = str()

    def post_api(self, header):
        url = "https://gorest.co.in/public-api/users"
        data = {"first_name": "Johny Z",
                "last_name": "Rocket",
                "gender": "male",
                "dob": "1970-08-12",
                "email": DocumentGenerator().email(),
                "phone": DocumentGenerator().phone(),
                "website": DocumentGenerator().url(),
                "address": "Platform 3/4 end of rainbow street",
                "status": "active"}
        response = requests.post(url, headers=header, json=data)

        self.user_id = json.dumps(response.json()['result']['id']).replace('"', '').rstrip('\n')
        response_code = json.dumps(response.json()['_meta']['code'])
        print(f'\nID #{self.user_id} POST with response {response_code}')
        return response_code

    def get_api(self):
        cont_type = 'json'
        token = 'TBi_Y27sxJ9XsBBmRgkb-oXSpjbWUdsotju1'
        url = f'https://gorest.co.in/public-api/users/{self.user_id}?_format={cont_type}&access-token={token}'
        response = requests.get(url)

        response_code = json.dumps(response.json()['_meta']['code'])
        print(f'\nID #{self.user_id} GET with response {response_code}')

        return response_code

    def delete_api(self, header):
        url = f'https://gorest.co.in/public-api/users/{self.user_id}'
        response = requests.delete(url, headers=header)

        response_code = json.dumps(response.json()['_meta']['code'])
        print(f'\nID #{self.user_id} DELETE with response {response_code}')

        return response_code
