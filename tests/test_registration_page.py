import pytest

from ..pages.home_page import HomePage
from ..pages.login_page import LoginPage
from ..pages.registration_page import RegistrationPage
from ..utils.data_generator import DataGenerator


class TestRegistration():
    
    @pytest.mark.register_user
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_signup_user(self, browser):
        page = LoginPage(browser)
        page.open()
        page.go_to_login_page() # Переход на страницу логина по нажатию на кнопку в навигации
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
        #Заполнение основных данных пользователя
        page.select_sex_checkbox(False,sex='f')
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
        # Проверка темы и сообщения об успешной регисрации
        page.should_be_correct_title()
        page.should_be_correct_congratilations()
        #Завершение регистрации, переход на домашнюю страницу по кнопке
        page.finish_signup()
        #Проверка на наличие кнопок для зарегестрированного пользователя
        page = HomePage(browser)
        page.check_username()
        page.delete_account() # Проверка удаления зарегистрированного пользователя по нажатию на кнопку
        page.is_link_correct('')

    @pytest.mark.register_exist_email
    @pytest.mark.negative
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_signup_user(self, browser):
        page = LoginPage(browser)
        page.open()
        page.go_to_login_page() # Переход на страницу логина по нажатию на кнопку в навигации
        # Проверки начальной страницы регистрации
        page.is_link_correct('login')
        page.should_be_new_user_text()
        page.should_be_signup_fields()
        page.fill_in_existing_email()
        page.fill_signup_name()
        page.click_signup_button()
        page.should_be_correct_signup_error_message()
        page.is_link_correct('signup')
            



