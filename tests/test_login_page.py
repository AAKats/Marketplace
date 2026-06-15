import allure
import pytest

from ..pages.home_page import HomePage
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

            page = HomePage(browser)
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

