import requests
from pprint import pprint
import json
from GenerateData import GenerateData


class ApiHelper:
    user_id = ''
    cont_type = 'json'
    token = 'TBi_Y27sxJ9XsBBmRgkb-oXSpjbWUdsotju1'
    gen = GenerateData()

    def post_api(self, header):
        url = "https://gorest.co.in/public-api/users"
        data = self.gen.data()
        response = requests.post(url, headers=header, json=data)
        self.user_id = json.dumps(response.json()['result']['id']).replace('"', '').rstrip('\n')
        response_code = json.dumps(response.json()['_meta']['code'])
        print(f'POST response for ID #{self.user_id} -> {response_code}')
        # pprint(data)

        return response_code

    def put_api(self):
        url = f'https://gorest.co.in/public-api/users/' \
              f'{self.user_id}?_format={self.cont_type}&access-token={self.token}'
        data = self.gen.data()
        response = requests.put(url, data)
        response_code = json.dumps(response.json()['_meta']['code'])
        print(f'PUT response for ID #{self.user_id} -> {response_code}')
        # pprint(data)

        return response_code

    def get_api(self):
        url = f'https://gorest.co.in/public-api/users/' \
              f'{self.user_id}?_format={self.cont_type}&access-token={self.token}'
        response = requests.get(url)
        response_code = json.dumps(response.json()['_meta']['code'])
        print(f'GET response for ID #{self.user_id} -> {response_code}')

        return response_code

    def delete_api(self, header):
        url = f'https://gorest.co.in/public-api/users/{self.user_id}'
        response = requests.delete(url, headers=header)
        response_code = json.dumps(response.json()['_meta']['code'])
        print(f'DELETE response for ID #{self.user_id} -> {response_code}')

        return response_code
