import pytest


class TestCreateOrder:
    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        []
    ])
    def test_create_order_with_different_color_combinations(self, order_api, random_order_payload, color):
        random_order_payload['color'] = color
        response = order_api.create_order(random_order_payload)
        assert response.json()['track']
        assert response.status_code == 201
