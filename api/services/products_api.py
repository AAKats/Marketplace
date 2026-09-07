from urllib import response

import allure

from ..client import ApiClient

class ProductsApi(ApiClient):

    @allure.step("GET запрос списка всех товаров")
    def get_all_products(self):
        """Получение списка всех товаров"""
        response = self.get("/api/productsList")
        return response

    @allure.step("POST запрос к списку всех товаров")
    def post_all_products(self):
        """Отправка POST для списка всех товаров"""
        response = self.post("/api/productsList")
        return response

    @allure.step("GET запрос списка всех брендов")
    def get_all_brands(self):
        """Получение списка всех брендов"""
        response = self.get("/api/brandsList")
        return response

    @allure.step("PUT запрос к списку брендов")
    def put_all_brands(self):
        """Отправка PUT запроса к списку брендов"""
        response = self.put("/api/brandsList")
        return response

    @allure.step("POST запрос поиска товаров: {product_name}")
    def post_to_search_product(self, product_name: str=''):
        """Отправка POST для поиска товаров"""
        data = {"search_product": f"{product_name}"}
        response = self.post('/api/searchProduct',data)
        return response

    @allure.step("POST запрос поиска товаров без тела")
    def post_to_search_product_without_body(self):
        """Отправка POST запроса поиска товаров без тела"""
        response = self.post('/api/searchProduct')
        return response