class TestOrderList:
    def test_get_list_orders(self, order_api):
        response = order_api.get_list()
        assert response.json()['orders'][0]['track']