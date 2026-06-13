import pytest

from ..pages.home_page import HomePage


class TestHomePage():
    '''Тесты главной страницы сайта'''
    def test_contact_us_form(self, browser):
        page = HomePage(browser)
        page.open()
