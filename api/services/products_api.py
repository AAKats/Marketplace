from urllib import response

from ..client import ApiClient

class ProductsApi(ApiClient):

    def get_all_products(self):
        """Получение списка всех товаров"""
        response = self.get("/api/productsList")
        return response

    def post_all_products(self):
        """Отправка POST для списка всех товаров"""
        response = self.post("/api/productsList")
        return response

    def get_all_brands(self):
        """Получение списка всех брендов"""
        response = self.get("/api/brandsList")
        return response

    def put_all_brands(self):
        """Получение списка всех брендов"""
        response = self.put("/api/brandsList")
        return response

    def post_to_search_product(self, product_name: str=''):
        """Отправка POST для поиска товаров"""
        data = {"search_product": f"{product_name}"}
        response = self.post('/api/searchProduct',data)
        return response

    def post_to_search_product_without_body(self):
        """Отправка POST для поиска товаров"""
        response = self.post('/api/searchProduct')
        return response