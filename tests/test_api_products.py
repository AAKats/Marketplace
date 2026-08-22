import allure
import pytest

from api.assertions import assert_response_message, assert_brand_fields, assert_searched_products
from ..api.assertions import (
    assert_status_code,
    assert_response_code,
    assert_json_has_key,
    assert_products_not_empty,
    assert_product_fields,
)


class TestApiProducts:

    @allure.feature('Products API')
    @allure.story('Получение списка всех товаров')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.api
    @pytest.mark.api_products
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.get_all_products
    def test_get_all_products(self, products_api):
        response = products_api.get_all_products()

        assert_status_code(response, 200)
        data = response.json()
        assert_response_code(data, 200)
        assert_json_has_key(data, 'products')
        assert_products_not_empty(data['products'])
        for product in data['products']:
            assert_product_fields(product)

    @allure.feature('Products API')
    @allure.story('Отправка POST запроса к Products list api')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    @pytest.mark.api_products
    @pytest.mark.negative
    @pytest.mark.smoke
    @pytest.mark.post_all_products
    def test_post_all_products(self, products_api):
        response = products_api.post_all_products()

        assert_status_code(response, 200)
        data = response.json()
        assert_response_code(data, 405)
        assert_response_message(data, 'This request method is not supported.')

    @allure.feature('Products API')
    @allure.story('Получение списка всех брендов')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.api
    @pytest.mark.api_products
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.get_all_brands
    def test_get_all_brands(self, products_api):
        response = products_api.get_all_brands()

        assert_status_code(response, 200)
        data = response.json()
        assert_response_code(data, 200)
        assert_json_has_key(data, 'brands')
        assert_products_not_empty(data['brands'])
        for brand in data['brands']:
            assert_brand_fields(brand)

    @allure.feature('Products API')
    @allure.story('Отправка PUT запроса к Brands list api')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    @pytest.mark.api_products
    @pytest.mark.negative
    @pytest.mark.smoke
    @pytest.mark.put_all_brands
    def test_put_all_brands(self, products_api):
        response = products_api.put_all_brands()

        assert_status_code(response, 200)
        data = response.json()
        assert_response_code(data, 405)
        assert_response_message(data, 'This request method is not supported.')

    @allure.feature('Products API')
    @allure.story('Поиск товара по части имени')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    @pytest.mark.api_products
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.search_product
    @pytest.mark.xfail(reason='BUG!')
    @pytest.mark.parametrize('product_type',['top', 'jean', 'tshirt'])
    def test_search_product(self, products_api, product_type):
        response = products_api.post_to_search_product(product_type)
        print(response)
        assert_status_code(response, 200)
        data = response.json()
        assert_response_code(data, 200)
        assert_searched_products(data, 200, product_type)

    @allure.feature('Products API')
    @allure.story('Поиск без тела запроса')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    @pytest.mark.api_products
    @pytest.mark.negative
    @pytest.mark.smoke
    @pytest.mark.blank_search_product
    def test_blank_search_product(self, products_api):
        response = products_api.post_to_search_product_without_body()
        print(response)
        assert_status_code(response, 200)
        data = response.json()
        assert_response_code(data, 400)
        assert_response_message(data, 'Bad request, search_product parameter is missing in POST '
                                      'request.')
