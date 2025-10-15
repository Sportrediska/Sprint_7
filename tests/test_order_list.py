import allure


class TestOrderList:
    @allure.title("Получение списка заказов")
    @allure.description("Проверка что в теле ответа возвращается список заказов")
    def test_get_list_orders(self, order_api):
        with allure.step("Получить список заказов"):
            response = order_api.get_list()

        with allure.step("Проверить наличие заказов в ответе"):
            assert response.json()['orders'][0]['track']
