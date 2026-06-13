import pytest

from ..pages.home_page import HomePage


class TestHomePage():
    '''Тесты главной страницы сайта'''

    @pytest.mark.positive
    @pytest.mark.ui
    @pytest.mark.subscribe
    @pytest.mark.subscribe_from_home
    def test_contact_us_form(self, browser):
        page = HomePage(browser)
        page.open()
        page.is_link_correct('')
        page.should_be_correct_subscription_text()
        page.input_subscribe_email()
        page.click_subscribe()
        page.should_be_success_subscribe_alert()

