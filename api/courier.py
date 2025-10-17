import requests
from url import BASE_URL


class CourierApi:

    def __init__(self):
        self.base_url = BASE_URL

    def login_courier(self, payload):
        return requests.post(self.base_url + '/api/v1/courier/login', json=payload)

    def delete_courier(self, courier_id):
        return requests.delete(self.base_url + f"/api/v1/courier/{courier_id}")

    def create_courier(self, payload):
        return requests.post(self.base_url + '/api/v1/courier', json=payload)
