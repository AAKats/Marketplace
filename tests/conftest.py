import pytest
from selenium import webdriver
from ..api.services.user_api import UserApi

@pytest.fixture(scope="function")
def browser():
    '''Фикстура запуска браузера для UI тестов'''
    # Настройка драйвера
    options = webdriver.ChromeOptions()

    # options.add_argument("--headless")

    browser = webdriver.Chrome(options=options)
    browser.execute_cdp_cmd('Network.setBlockedURLs', {
        'urls': ['*fundingchoicesmessages.google.com*', '*pagead2.googlesyndication.com*']
    })
    browser.execute_cdp_cmd('Network.enable', {})

    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture(scope="session")
def api_client():
    """Фикстура для API запросов"""
    return UserApi(base_url="https://automationexercise.com")
