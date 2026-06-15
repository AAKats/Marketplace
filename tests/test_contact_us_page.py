import allure
import pytest

from utils.data_generator import DataGenerator
from ..pages.contact_us_page import ContactUsPage


class TestContacUsPage():
    '''Тесты страницы обратной связи'''

    @allure.feature('Contact Us')
    @allure.story('Отправка формы обратной связи')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.contact_us
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_contact_us_form(self, browser):
        page = ContactUsPage(browser)
        page.open()
        page.is_link_correct()
        page.go_to_contact_us_page()
        page.should_be_correct_title()
        page.should_be_correct_second_title()
        DataGenerator.generate_data_for_registration(['email','first_name'])
        page.fill_in_name_field()
        page.fill_in_email_field()
        page.fill_in_subject_field()
        page.fill_in_message_field()
        page.upload_contact_us_file()
        page.click_submit_button()
        page.accept_alert()
        page.should_be_correct_success_message()
        page.go_to_home_page()
        page.is_link_correct()


