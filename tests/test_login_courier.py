class TestLoginCourier:
    def test_authorization_success(self, courier_api, random_courier_payload):
        courier_api.create_courier(payload=random_courier_payload)
        response = courier_api.login_courier(random_courier_payload)
        assert response.status_code == 200
        courier_api.delete_courier(response.json()['id'])

    def test_authorization_no_required_fields_error(self, courier_api, random_courier_payload):
        courier_api.create_courier(payload=random_courier_payload)
        response = courier_api.login_courier(payload={})
        assert response.status_code == 400
        response = courier_api.login_courier(random_courier_payload)
        courier_api.delete_courier(response.json()['id'])

    def test_authorization_incorrect_password_error(self, courier_api, random_courier_payload):
        courier_api.create_courier(payload=random_courier_payload)
        response = courier_api.login_courier(payload={
            'login': random_courier_payload['login'],
            'password': 'kaviryaka'
        })
        assert response.status_code == 404
        response = courier_api.login_courier(random_courier_payload)
        courier_api.delete_courier(response.json()['id'])

    def test_empty_required_login_error(self, courier_api, random_courier_payload):
        courier_api.create_courier(payload=random_courier_payload)
        response = courier_api.login_courier(payload={
            'password': random_courier_payload['password']
        })
        assert response.status_code == 400
        response = courier_api.login_courier(random_courier_payload)
        courier_api.delete_courier(response.json()['id'])

    def test_login_not_exist_courier_error(self, courier_api, random_courier_payload):
        response = courier_api.login_courier(payload=random_courier_payload)
        assert response.status_code == 404

    def test_authorization_returns_id(self, courier_api, random_courier_payload):
        courier_api.create_courier(payload=random_courier_payload)
        response = courier_api.login_courier(random_courier_payload)
        assert response.json()['id']
        courier_api.delete_courier(response.json()['id'])
