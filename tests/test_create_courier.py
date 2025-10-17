import allure

class TestCreateCourier:
    @allure.title("Успешное создание курьера")
    @allure.description("Проверка что курьера можно создать")
    def test_create_success(self, courier_api, random_courier_payload, login_delete_courier):
        response = courier_api.create_courier(payload={
            "login": random_courier_payload['login'],
            "password": random_courier_payload['password'],
            "firstName": random_courier_payload['firstName']
        })
        assert response.json() != []
        login_delete_courier(random_courier_payload)

    @allure.title("Нельзя создать двух одинаковых курьеров")
    @allure.description("Проверка что нельзя создать курьера с одинаковыми данными")
    def test_no_create_same(self, new_courier, courier_api):
        response = courier_api.create_courier(payload={
            "login": new_courier[0],
            "password": new_courier[1],
            "firstName": new_courier[2]
        })
        assert response.status_code == 409

    @allure.title("Создание курьера без обязательных полей")
    @allure.description("Проверка что без обязательных полей возвращается ошибка")
    def test_create_no_required_fields_error(self, courier_api):
        response = courier_api.create_courier(payload={})
        assert response.status_code == 400

    @allure.title("Правильный код ответа при создании курьера")
    @allure.description("Проверка что успешный запрос возвращает статус 201")
    def test_status_code(self, new_courier_response):
        assert new_courier_response.status_code == 201

    @allure.title("Тело ответа при успешном создании курьера")
    @allure.description("Проверка что успешный запрос возвращает {'ok': true}")
    def test_return_success_body(self, new_courier_response):
        assert new_courier_response.json() == {'ok': True}

    @allure.title("Ошибка при отсутствии обязательного поля firstName")
    @allure.description("Проверка что без firstName возвращается ошибка")
    def test_empty_required_firstname_return_error(self, courier_api, random_courier_payload):
        response = courier_api.create_courier(payload={
            "login": random_courier_payload['login'],
            "password": random_courier_payload['password']
        })
        assert response.status_code == 400

    @allure.title("Ошибка при создании курьера с существующим логином")
    @allure.description("Проверка что нельзя создать курьера с уже существующим логином")
    def test_create_user_duplicate_login(self, new_courier, courier_api):
        response = courier_api.create_courier(payload={
            "login": new_courier[0],
            "password": new_courier[1] + 'test',
            "firstName": new_courier[2] + 'test'
        })
        assert response.status_code == 409