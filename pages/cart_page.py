import allure

from selenium.common import TimeoutException

from locators import CartPageLocators
from .products_page import ProductsPage
from ..pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, browser, added_products=None, quantity = 0):
        super().__init__(browser)
        if isinstance(added_products, dict):
            added_products = [added_products]
        self.added_products = added_products or []
        self.quantity = quantity

    '''Методы для страницы корзины товаров'''

    @allure.step("Проверка количества товаров в корзине")
    def cart_should_contain_correct_count_of_products(self, count : int = None):
        if count == None:
            self.is_element_present(CartPageLocators.PRODUCTS_IN_CART)
            products_count_in_cart = len(self.find_elements(CartPageLocators.PRODUCTS_IN_CART))
            assert products_count_in_cart == len(self.added_products), f'Count of products in cart {products_count_in_cart} is not equal to count of added products {len(self.added_products)}'
            print(f'Count of products in cart {products_count_in_cart} is equal to count of added products {len(self.added_products)}')
        else:
            try:
                products = self.find_elements(CartPageLocators.PRODUCTS_IN_CART, time=3)
            except TimeoutException:
                self.browser.refresh()
                products = self.find_elements(CartPageLocators.PRODUCTS_IN_CART)
            products_count_in_cart = len(self.find_elements(CartPageLocators.PRODUCTS_IN_CART))
            assert products_count_in_cart == count, f'Count of products in cart {products_count_in_cart} is not equal to count of added products {count}'
            print(f'Count of products in cart {products_count_in_cart} is equal to count of added products {count}')

    @allure.step("Проверка цены товаров в корзине")
    def check_product_price(self):
        products_prices = self.find_elements(CartPageLocators.PRODUCT_PRICE_IN_CART)
        products_names = self.find_elements(CartPageLocators.PRODUCT_NAME_IN_CART)
        for _ in range(len(self.added_products)):
            product_price = self.added_products[_]['price']
            product_price_in_cart = products_prices[_].text[4:]
            assert product_price == product_price_in_cart, f'Product {products_names[_].text} price in cart: {product_price_in_cart} does not match added price: {product_price}'
            print(f'Product {products_names[_].text} price in cart: {product_price_in_cart} matches added price: {product_price}')

    @allure.step("Проверка названий товаров в корзине")
    def check_product_name(self):
        names_in_cart = []
        products_names = self.find_elements(CartPageLocators.PRODUCT_NAME_IN_CART)
        for name in products_names:
            names_in_cart.append(name.text)
        for _ in range(len(self.added_products)):
            product_name = self.added_products[_]['name']
            assert product_name in names_in_cart, f'Имя товара: {product_name} отсутствует в корзине: {', '.join(names_in_cart)}'
            print(f'Имя товара: {product_name} Найдено в корзине: {', '.join(names_in_cart)}')

    @allure.step("Проверка количества каждого товара в корзине")
    def check_product_quantity(self):
        products_quantities = self.find_elements(CartPageLocators.PRODUCT_QUANTITY_IN_CART)
        products_names = self.find_elements(CartPageLocators.PRODUCT_NAME_IN_CART)
        if self.quantity == 0:
            for _ in range(len(self.added_products)):
                if self.added_products[_]['name'] == products_names[_].text:
                    product_quantity = self.added_products[_]['quantity']
                    product_quantity_in_cart = int(products_quantities[_].text)
                    assert product_quantity == product_quantity_in_cart, f'Количество товара {products_names[_].text} в корзине: {product_quantity_in_cart} не равно количеству добавленного товара: {product_quantity}'
                    print(f'Количество товара {products_names[_].text} в корзине: {product_quantity_in_cart} равно количеству добавленного товара: {product_quantity}')
        else:
            for _ in range(len(self.added_products)):
                if self.added_products[_]['name'] == products_names[_].text:
                    product_quantity = self.quantity
                    product_quantity_in_cart = int(products_quantities[_].text)
                    assert product_quantity == product_quantity_in_cart, f'Количество товара {products_names[_].text} в корзине: {product_quantity_in_cart} не равно количеству добавленного товара: {product_quantity}'
                    print(f'Количество товара {products_names[_].text} в корзине: {product_quantity_in_cart} равно количеству добавленного товара: {product_quantity}')

    @allure.step("Проверка общей стоимости товаров в корзине")
    def check_product_total_price(self):
        products_total_prices = self.find_elements(CartPageLocators.PRODUCT_TOTAL_PRICE_IN_CART)
        products_names = self.find_elements(CartPageLocators.PRODUCT_NAME_IN_CART)
        for _ in range(len(self.added_products)):
            if self.added_products[_]['name'] == products_names[_].text:
                product_total_price = int(self.added_products[_]['price']) * int(self.added_products[_]['quantity'])
                product_total_price_in_cart = int(products_total_prices[_].text[4:])
                assert product_total_price == product_total_price_in_cart, f'Общая цена товара в корзине: {product_total_price_in_cart} не равна общей цене добавленного товара: {product_total_price}'
                print(f'Общая цена товара в корзине: {product_total_price_in_cart} не равна общей цене добавленного товара: {product_total_price}')
