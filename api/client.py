import requests


class ScooterApi:

    def __init__(self):
        self.base_url = 'https://qa-scooter.praktikum-services.ru'

    def login_courier(self, payload):
        return requests.post(self.base_url + '/api/v1/courier/login', data=payload)

    def delete_courier(self, courier_id):
        return requests.delete(self.base_url + f"/api/v1/courier/{courier_id}")

    def create_courier(self, payload):
        return requests.post(self.base_url + '/api/v1/courier', data=payload)
