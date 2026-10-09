import os

import allure
import pytest
from selenium import webdriver
from ..api.services.user_api import UserApi
from ..api.services.products_api import ProductsApi
from utils.data_generator import DataGenerator


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Запуск браузера в headless-режиме",
    )


def is_headless(config) -> bool:
    if config.getoption("--headless"):
        return True
    return os.getenv('HEADLESS', '').lower() in ('true', '1')


@pytest.fixture(scope="function")
def browser(request):
    '''Фикстура запуска браузера для UI тестов'''
    # Настройка драйвера
    options = webdriver.ChromeOptions()

    if is_headless(request.config):
        options.add_argument("--headless")

    browser = webdriver.Chrome(options=options)

    '''Удаление GDPR cookie popup '''
    browser.execute_cdp_cmd('Network.enable', {})
    browser.execute_cdp_cmd('Network.setBlockedURLs', {
        'urls': ['*fundingchoicesmessages.google.com*', '*pagead2.googlesyndication.com*']
    })

    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def api_client():
    """Фикстура для API запросов"""
    return UserApi(base_url="https://automationexercise.com")


@pytest.fixture(scope="session")
def products_api():
    """Фикстура для API запросов к продуктам"""
    return ProductsApi(base_url="https://automationexercise.com")


@pytest.fixture(scope="session")
def existing_user(api_client):
    """Создаёт пользователя через API для тестов, которым нужен существующий аккаунт"""
    DataGenerator.generate_data_for_registration()
    response = api_client.create_account()
    assert response.status_code == 200, \
        f'Не удалось создать пользователя через API: {response.status_code} {response.text}'
    profile = DataGenerator.get_registration_data()
    DataGenerator.set_existing_user(profile)
    yield profile
    try:
        api_client.delete_registered_user(profile['email'], profile['password'])
        print('Тестовый пользователь удалён')
    except Exception as e:
        print(f'Не удалось удалить тестового пользователя: {e}')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        if "browser" in item.fixturenames:
            browser = item.funcargs["browser"]
            allure.attach(
                browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )


def pytest_sessionfinish(session):
    """Запись environment.properties после завершения сессии"""
    import os
    results_dir = "allure-results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    with open(os.path.join(results_dir, "environment.properties"), "w", encoding="utf-8") as f:
        f.write("Browser=Chrome\n")
        f.write("Browser.Version=latest\n")
        f.write("URL=https://automationexercise.com\n")
        f.write("Framework=pytest\n")
        f.write("Report=Allure\n")


@pytest.fixture(scope="function")
def browser_download(request):
    """Фикстура браузера с автоскачиванием файлов"""

    options = webdriver.ChromeOptions()
    download_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'temp')
    os.makedirs(download_dir, exist_ok=True)

    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
    }
    options.add_experimental_option("prefs", prefs)

    if is_headless(request.config):
        options.add_argument("--headless")

    browser = webdriver.Chrome(options=options)
    browser.execute_cdp_cmd('Network.enable', {})
    browser.execute_cdp_cmd('Network.setBlockedURLs', {
        'urls': ['*fundingchoicesmessages.google.com*', '*pagead2.googlesyndication.com*']
    })
    browser.maximize_window()
    yield browser, download_dir
    browser.quit()
    # Очистка папки после теста
    for f in os.listdir(download_dir):
        os.remove(os.path.join(download_dir, f))
