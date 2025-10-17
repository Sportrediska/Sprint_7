import requests

from url import BASE_URL


class OrderApi:
    def __init__(self):
        self.base_url = BASE_URL

    def create_order(self, payload):
        return requests.post(self.base_url + '/api/v1/orders', json=payload)

    def get_list(self):
        return requests.get(self.base_url + '/api/v1/orders')