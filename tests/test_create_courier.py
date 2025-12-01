import allure

class TestCreateCourier:
    @allure.title("Успешное создание курьера")
    @allure.description("Проверка что курьера можно создать")
    def test_create_success(self, courier_api, random_courier_payload, login_delete_courier):
        with allure.step("Создать курьера с валидными данными"):
            response = courier_api.create_courier(payload={
                "login": random_courier_payload['login'],
                "password": random_courier_payload['password'],
                "firstName": random_courier_payload['firstName']
            })
        with allure.step("Проверить что курьер создан"):
            assert response.json() != []
        with allure.step("Удалить тестового курьера"):
            login_delete_courier(random_courier_payload)

    @allure.title("Нельзя создать двух одинаковых курьеров")
    @allure.description("Проверка что нельзя создать курьера с одинаковыми данными")
    def test_no_create_same(self, new_courier, courier_api):
        with allure.step("Попытаться создать курьера с существующими данными"):
            response = courier_api.create_courier(payload={
                "login": new_courier[0],
                "password": new_courier[1],
                "firstName": new_courier[2]
            })
        with allure.step("Проверить ошибку конфликта"):
            assert response.status_code == 409

    @allure.title("Создание курьера без обязательных полей")
    @allure.description("Проверка что без обязательных полей возвращается ошибка")
    def test_create_no_required_fields_error(self, courier_api):
        with allure.step("Создать курьера с пустым телом запроса"):
            response = courier_api.create_courier(payload={})
        with allure.step("Проверить ошибку валидации"):
            assert response.status_code == 400

    @allure.title("Создание курьера без обязательного поля login")
    @allure.description("Проверка что без login возвращается ошибка")
    def test_create_no_required_login_return_error(self, courier_api, random_courier_payload):
        with allure.step("Создать курьера без поля login"):
            response = courier_api.create_courier(payload={
                "password": random_courier_payload['password'],
                "firstName": random_courier_payload['firstName']
            })
        with allure.step("Проверить ошибку валидации"):
            assert response.status_code == 400

    @allure.title("Создание курьера без обязательного поля firstName")
    @allure.description("Проверка что без firstName возвращается ошибка")
    def test_create_no_required_firstname_return_error(self, courier_api, random_courier_payload):
        with allure.step("Создать курьера без поля firstName"):
            response = courier_api.create_courier(payload={
                "login": random_courier_payload['login'],
                "password": random_courier_payload['password']
            })
        with allure.step("Проверить ошибку валидации"):
            assert response.status_code == 400

    @allure.title("Создание курьера без обязательного поля password")
    @allure.description("Проверка что без password возвращается ошибка")
    def test_create_no_required_password_return_error(self, courier_api, random_courier_payload):
        with allure.step("Создать курьера без поля password"):
            response = courier_api.create_courier(payload={
                "login": random_courier_payload['login'],
                "firstName": random_courier_payload['firstName']
            })
        with allure.step("Проверить ошибку валидации"):
            assert response.status_code == 400

    @allure.title("Правильный код ответа при создании курьера")
    @allure.description("Проверка что успешный запрос возвращает статус 201")
    def test_status_code(self, courier_api, random_courier_payload, login_delete_courier):
        with allure.step("Создать курьера с валидными данными"):
            response = courier_api.create_courier(payload={
                "login": random_courier_payload['login'],
                "password": random_courier_payload['password'],
                "firstName": random_courier_payload['firstName']
            })
        with allure.step("Проверить статус код 201"):
            assert response.status_code == 201
        with allure.step("Удалить тестового курьера"):
            login_delete_courier(random_courier_payload)

    @allure.title("Тело ответа при успешном создании курьера")
    @allure.description("Проверка что успешный запрос возвращает {'ok': true}")
    def test_return_success_body(self, courier_api, random_courier_payload, login_delete_courier):
        with allure.step("Создать курьера с валидными данными"):
            response = courier_api.create_courier(payload={
                "login": random_courier_payload['login'],
                "password": random_courier_payload['password'],
                "firstName": random_courier_payload['firstName']
            })
        with allure.step("Проверить тело ответа"):
            assert response.json() == {"ok": True}
        with allure.step("Удалить тестового курьера"):
            login_delete_courier(random_courier_payload)

    @allure.title("Ошибка при создании курьера с существующим логином")
    @allure.description("Проверка что нельзя создать курьера с уже существующим логином")
    def test_create_user_duplicate_login(self, new_courier, courier_api):
        with allure.step("Попытаться создать курьера с существующим логином"):
            response = courier_api.create_courier(payload={
                "login": new_courier[0],
                "password": new_courier[1] + 'test',
                "firstName": new_courier[2] + 'test'
            })
        with allure.step("Проверить ошибку конфликта"):
            assert response.status_code == 409