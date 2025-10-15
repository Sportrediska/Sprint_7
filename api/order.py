import requests


class OrderApi:
    def __init__(self):
        self.base_url = 'https://qa-scooter.praktikum-services.ru'

    def create_order(self, payload):
        return requests.post(self.base_url + '/api/v1/orders', json=payload)
