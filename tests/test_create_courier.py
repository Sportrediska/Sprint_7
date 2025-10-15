class TestCreateCourier:
    def test_create_success(self, new_courier):
        assert new_courier != {}

    def test_no_create_same(self, new_courier, scooter_api):
        response = scooter_api.create_courier(payload={
            "login": new_courier[0],
            "password": new_courier[1],
            "firstName": new_courier[2]
        })
        assert response.status_code == 409

    def test_create_only_required_fields(self, scooter_api):
        response = scooter_api.create_courier(payload={})
        assert response.status_code == 400

    def test_status_code(self, new_courier_response):
        assert new_courier_response.status_code == 201

    def test_return_success_body(self, new_courier_response):
        assert new_courier_response.json() == {'ok': True}

    def test_empty_required_firstname_return_error(self, scooter_api, random_courier_payload):
        response = scooter_api.create_courier(payload={
            "login": random_courier_payload['login'],
            "password": random_courier_payload['password']
        })
        assert response == 400

    def test_create_user_duplicate_login(self, new_courier, scooter_api):
        response = scooter_api.create_courier(payload={
            "login": new_courier[0],
            "password": new_courier[1] + 'test',
            "firstName": new_courier[2] + 'test'
        })
        assert response.status_code == 409
