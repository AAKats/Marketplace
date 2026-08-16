import allure
import pytest

from ..pages.payment_page import PaymentPage
from ..pages.checkout_page import CheckoutPage
from ..pages.products_page import ProductsPage
from ..pages.login_page import LoginPage


class TestLogin():
    @allure.feature('Login')
    @allure.story('Успешный вход')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.login_user
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_login_user(self, browser):
            page = LoginPage(browser)
            page.open()
            page.go_to_login_page() # Переход на страницу логина по нажатию на кнопку в навигации
            # Проверки начальной страницы авторизации
            page.is_link_correct('login')
            page.should_be_correct_login_title()
            page.should_be_login_fields()
            page.fill_in_email()
            page.fill_in_password()
            page.click_login_button()

            page.is_link_correct()
            page.check_username(True)
            page.logout()
            page.should_not_be_username()

    @allure.feature('Login')
    @allure.story('Вход с неверными данными')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.incorrect_login_user
    @pytest.mark.negative
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_incorrect_login_user(self, browser):
        page = LoginPage(browser)
        page.open()
        page.go_to_login_page()  # Переход на страницу логина по нажатию на кнопку в навигации
        # Проверки начальной страницы авторизации
        page.is_link_correct('login')
        page.should_be_correct_login_title()
        page.should_be_login_fields()
        page.fill_in_email('incorrect@mail.com')
        page.fill_in_password()
        page.click_login_button()
        page.should_be_correct_login_error_message()
        page.is_link_correct('login')
        page.should_not_be_username()

    @allure.feature('Login')
    @allure.story('Логин перед покупкой')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.login_before_checkout
    @pytest.mark.negative
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_login_before_checkout(self, browser):
        page = LoginPage(browser)
        page.open()
        page.is_link_correct()
        page.go_to_login_page()
        page.is_link_correct('login')
        page.fill_in_email()
        page.fill_in_password()
        page.click_login_button()

        page.is_link_correct()
        page.check_username(True)
        page = ProductsPage(browser)
        added_products = page.add_products_to_cart(False, False, 3,1)
        page.go_to_cart_page()
        page.is_link_correct('/view_cart')
        page = CheckoutPage(browser, added_products)
        page.click_proceed_to_checkout()
        page.check_delivery_details(login=True)
        page.check_billing_details(login=True)
        page.cart_should_contain_correct_count_of_products()
        page.check_product_price()
        page.check_product_name()
        page.check_product_quantity()
        page.check_product_total_price()
        page.fill_comment()
        page.place_order()
        page = PaymentPage(browser)
        page.fill_in_card_info()
        page.pay_and_confirm()
        page.should_be_correct_payment_success_message()