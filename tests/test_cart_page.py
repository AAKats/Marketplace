import allure
import pytest

from ..pages.products_page import ProductsPage
from ..pages.cart_page import CartPage


class TestCartPage():
    '''Тесты страницы корзины товаров'''

    @allure.feature('Cart')
    @allure.story('Подписка на рассылку со страницы корзины')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.positive
    @pytest.mark.ui
    @pytest.mark.subscribe
    @pytest.mark.subscribe_from_cart
    def test_subscribe_from_cart(self, browser):
        page = CartPage(browser)
        page.open()
        page.is_link_correct()
        page.go_to_cart_page()
        page.is_link_correct('view_cart')
        page.should_be_correct_subscription_text()
        page.input_subscribe_email()
        page.click_subscribe()
        page.should_be_success_subscribe_alert()

    @allure.feature('Cart')
    @allure.story('Добавление товаров в корзину и проверка')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.positive
    @pytest.mark.ui
    @pytest.mark.purchase
    @pytest.mark.add_products_in_cart
    def test_add_products_in_cart(self,browser):
        page = ProductsPage(browser)
        page.open()
        page.is_link_correct()
        page.go_to_products_page()
        added_products = page.add_products_to_cart(False,3,2)
        page = CartPage(browser,added_products)
        page.cart_should_contain_correct_count_of_products()
        page.check_product_price()
        page.check_product_name()
        page.check_product_quantity()
        page.check_product_total_price()





