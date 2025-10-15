import pytest
import random
import string
from faker import Faker
from api.courier import CourierApi
from api.order import OrderApi


@pytest.fixture
def courier_api():
    return CourierApi()


@pytest.fixture
def order_api():
    return OrderApi()


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
        'login': login,
        'password': password,
        'firstName': first_name
    }


@pytest.fixture
def new_courier(courier_api, random_courier_payload):
    login_pass = []

    response = courier_api.create_courier(random_courier_payload)

    if response.status_code == 201:
        login_pass.append(random_courier_payload['login'])
        login_pass.append(random_courier_payload['password'])
        login_pass.append(random_courier_payload['firstName'])

    yield login_pass

    if login_pass:
        response = courier_api.login_courier(payload={
            'login': login_pass[0],
            'password': login_pass[1]
        })
        courier_api.delete_courier(courier_id=response.json()['id'])


@pytest.fixture
def new_courier_response(courier_api, random_courier_payload):
    response = courier_api.create_courier(random_courier_payload)

    yield response

    if response.status_code == 201:
        response = courier_api.login_courier(payload={
            'login': random_courier_payload['login'],
            'password': random_courier_payload['password']
        })
        courier_api.delete_courier(courier_id=response.json()['id'])


@pytest.fixture
def random_order_payload():
    fake = Faker('ru_RU')
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": fake.random_int(1, 20),
        "phone": fake.phone_number(),
        "rentTime": fake.random_int(1, 10),
        "deliveryDate": fake.date_between(start_date='today', end_date='+30d').strftime('%Y-%m-%d'),
        "comment": fake.text(max_nb_chars=50)
    }
