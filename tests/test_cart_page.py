from time import sleep

import allure
import pytest

from ..pages.payment_page import PaymentPage
from ..pages.checkout_page import CheckoutPage
from ..pages.home_page import HomePage
from ..pages.login_page import LoginPage
from ..pages.registration_page import RegistrationPage
from ..utils.data_generator import DataGenerator
from ..pages.product_page import ProductPage
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

    @allure.feature('Cart')
    @allure.story('Добавление товара в корзину со страницы товара и проверка')
    @pytest.mark.positive
    @pytest.mark.ui
    @pytest.mark.purchase
    @pytest.mark.add_product_in_cart_from_product_page
    def test_add_product_in_cart_from_product_page(self,browser):
        page = ProductsPage(browser)
        page.open()
        page.is_link_correct()
        page.go_to_products_page()
        product_details = page.open_random_product()
        page.is_link_correct(f'product_details/{product_details["id"]}')
        page = ProductPage(browser)
        quantity = page.select_quantity_of_product()
        page.add_product_to_cart()
        page.go_to_cart_via_modal()
        page = CartPage(browser,product_details,quantity)
        page.cart_should_contain_correct_count_of_products(1)
        page.check_product_name()
        page.check_product_price()
        page.check_product_quantity()

    @allure.feature('Cart')
    @allure.feature('Register')
    @allure.story('Регистрация со страницы корзины')
    @pytest.mark.positive
    @pytest.mark.ui
    @pytest.mark.purchase
    @pytest.mark.register_while_checkout
    def test_register_while_checkout(self,browser):
        page = ProductsPage(browser)
        page.open()
        page.is_link_correct()
        page.go_to_products_page()
        added_products = page.add_products_to_cart(False, False, 2,2)
        page.go_to_cart_page()
        page.is_link_correct('/view_cart')
        page = CartPage(browser)
        page.click_proceed_to_checkout()
        page.register_via_modal()
        page = LoginPage(browser)
        # Проверки начальной страницы регистрации
        page.is_link_correct('login')
        page.should_be_new_user_text()
        page.should_be_signup_fields()
        # Генерация данных для регистрации
        datagen = DataGenerator()
        datagen.generate_data_for_registration()
        # Заполнение первичных данных для регистрации
        page.fill_signup_email()
        page.fill_signup_name()
        page.click_signup_button()

        page = RegistrationPage(browser)
        page.should_be_signup_url()
        page.should_be_account_information_text()
        # Проверка корректности введенных первичных данных при регистрации
        page.check_email_field()
        page.check_name_field()
        # Заполнение основных данных пользователя
        page.select_sex_checkbox(True)
        page.fill_in_password()
        page.fill_in_date_of_birth()
        page.select_newsletter_checkbox(True)
        page.select_special_offers_checkbox(True)
        # Заполнение дополнительных данных о пользователе
        page.fill_in_first_name()
        page.fill_in_last_name()
        page.fill_in_company()
        page.fill_in_address_1()
        page.fill_in_address_2()
        page.select_country()
        page.fill_in_state()
        page.fill_in_city()
        page.fill_in_zipcode()
        page.fill_in_mobile_number()
        # Нажатие на кнопку завершения регистрации и проверка корректности перехода на страницу с сообщением об успешной регистрации
        page.finish_account_creation()
        # Проверка темы и сообщения об успешной регистрации
        page.should_be_correct_title()
        page.should_be_correct_congratilations()
        # Завершение регистрации, переход на домашнюю страницу по кнопке
        page.finish_signup()
        # Проверка на наличие кнопок для зарегистрированного пользователя
        page = HomePage(browser)
        page.check_username()
        page.go_to_cart_page()
        page.is_link_correct('/view_cart')
        page = CheckoutPage(browser,added_products)
        page.click_proceed_to_checkout()
        page.check_delivery_details()
        page.check_billing_details()
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
        page = HomePage(browser)
        page.delete_account()  # Проверка удаления зарегистрированного пользователя по нажатию на кнопку
        page.is_link_correct('')








