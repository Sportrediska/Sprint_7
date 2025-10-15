import pytest
import random
import string

from api.client import ScooterApi


@pytest.fixture
def scooter_api():
    return ScooterApi()


@pytest.fixture
def random_courier_payload():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }



@pytest.fixture
def new_courier(scooter_api, random_courier_payload):
    login_pass = []

    response = scooter_api.create_courier(random_courier_payload)

    if response.status_code == 201:
        login_pass.append(random_courier_payload['login'])
        login_pass.append(random_courier_payload['password'])
        login_pass.append(random_courier_payload['firstName'])

    yield login_pass

    if login_pass:
        response = scooter_api.login_courier(payload={
            "login": login_pass[0],
            "password": login_pass[1]
        })
        scooter_api.delete_courier(courier_id=response.json()['id'])


@pytest.fixture
def new_courier_response(scooter_api, random_courier_payload):
    response = scooter_api.create_courier(random_courier_payload)

    yield response

    if response.status_code == 201:
        response = scooter_api.login_courier(payload={
            "login": random_courier_payload['login'],
            "password": random_courier_payload['password']
        })
        scooter_api.delete_courier(courier_id=response.json()['id'])
