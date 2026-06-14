import pytest

from ..pages.cart_page import CartPage


class TestCartPage():
    '''Тесты страницы корзины товаров'''

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

