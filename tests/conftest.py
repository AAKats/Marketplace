import pytest
from selenium import webdriver
from api.services.user_api import UserApi

@pytest.fixture(scope="function")
def driver():
    # Настройка драйвера
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def api_client():
    """Фикстура для API запросов"""
    return UserApi(base_url="https://automationexercise.com")