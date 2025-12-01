import allure
import pytest


class TestCreateOrder:
    @allure.title("Создание заказа с разными цветами: {color}")
    @allure.description("Проверка создания заказа с разными вариантами цветов")
    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        []
    ])
    def test_create_order_with_different_color_combinations(self, order_api, random_order_payload, color):
        with allure.step(f"Установить цвет заказа: {color}"):
            random_order_payload['color'] = color

        with allure.step("Создать заказ"):
            response = order_api.create_order(random_order_payload)

        with allure.step("Проверить код ответа"):
            assert response.status_code == 201

        with allure.step("Проверить наличие track в ответе"):
            assert response.json()['track']
