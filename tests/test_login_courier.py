import allure


class TestLoginCourier:
    @allure.title("Успешная авторизация курьера")
    @allure.description("Проверка что курьер может авторизоваться")
    def test_authorization_success(self, courier_api, random_courier_payload):
        with allure.step("Создать тестового курьера"):
            courier_api.create_courier(payload=random_courier_payload)

        with allure.step("Выполнить авторизацию"):
            response = courier_api.login_courier(random_courier_payload)

        with allure.step("Проверить успешную авторизацию"):
            assert response.status_code == 200

        with allure.step("Удалить тестового курьера"):
            courier_api.delete_courier(response.json()['id'])

    @allure.title("Ошибка авторизации без обязательных полей")
    @allure.description("Проверка что для авторизации нужны все обязательные поля")
    def test_authorization_no_required_fields_error(self, courier_api, random_courier_payload):
        courier_api.create_courier(payload=random_courier_payload)
        response = courier_api.login_courier(payload={})
        assert response.status_code == 400
        response = courier_api.login_courier(random_courier_payload)
        courier_api.delete_courier(response.json()['id'])

    @allure.title("Ошибка авторизации с неправильным паролем")
    @allure.description("Проверка ошибки при неправильном пароле")
    def test_authorization_incorrect_password_error(self, courier_api, random_courier_payload):
        courier_api.create_courier(payload=random_courier_payload)
        response = courier_api.login_courier(payload={
            'login': random_courier_payload['login'],
            'password': 'kaviryaka'
        })
        assert response.status_code == 404
        response = courier_api.login_courier(random_courier_payload)
        courier_api.delete_courier(response.json()['id'])

    @allure.title("Ошибка авторизации без логина")
    @allure.description("Проверка ошибки при отсутствии логина")
    def test_empty_required_login_error(self, courier_api, random_courier_payload):
        courier_api.create_courier(payload=random_courier_payload)
        response = courier_api.login_courier(payload={
            'password': random_courier_payload['password']
        })
        assert response.status_code == 400
        response = courier_api.login_courier(random_courier_payload)
        courier_api.delete_courier(response.json()['id'])

    @allure.title("Ошибка авторизации несуществующего курьера")
    @allure.description("Проверка ошибки при авторизации под несуществующим пользователем")
    def test_login_not_exist_courier_error(self, courier_api, random_courier_payload):
        response = courier_api.login_courier(payload=random_courier_payload)
        assert response.status_code == 404

    @allure.title("Успешная авторизация возвращает id")
    @allure.description("Проверка что успешный запрос возвращает id курьера")
    def test_authorization_returns_id(self, courier_api, random_courier_payload):
        courier_api.create_courier(payload=random_courier_payload)
        response = courier_api.login_courier(random_courier_payload)
        assert response.json()['id']
        courier_api.delete_courier(response.json()['id'])
