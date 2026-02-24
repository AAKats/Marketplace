from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from ..locators import BasePageLocators


class BasePage:
    def __init__(self, browser):
        self.driver = browser
        self.base_url = "https://automationexercise.com"

    '''Основные методы для ui'''
    def find(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Element not found: {locator}"
        )

    def open(self, url):
        self.driver.get(f"{self.base_url}{url}")

    '''Методы для перехода по страницам сайта через панель навигации'''
    def go_to_login_page(self):
        self.find(BasePageLocators.SIGNUP_LOGIN_BUTTON).click()

    def go_to_products_page(self):
        self.find(BasePageLocators.PRODUCTS_BUTTON).click()

    def go_to_cart_page(self):
        self.find(BasePageLocators.CART_BUTTON).click()

    def go_to_home_page(self):
        self.find(BasePageLocators.HOME_BUTTON).click()

    '''Методы для проверки наличия или отсутствия элемента на странице'''
    def is_element_present(self, locator):
        try:
            self.find(locator)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((locator)))
        except TimeoutException:
            return True
        return False
    
    '''Методы для выпадающих списков'''
    def select_by_value(self, locator, value):
        try:
            Select(self.find(locator)).select_by_value(value)
        except NoSuchElementException as element:
            print(f"Элемент не найден в выпадающем списке: {element}")

    # Метод для проверки корректности ссылки в поисковой строке
    def is_link_correct(self, value):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains(value))
            print(f'{value.capitalize()} link is correct')
        except TimeoutException:
            raise AssertionError(f'Current link is not {value} link')
