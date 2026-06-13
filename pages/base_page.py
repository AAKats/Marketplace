from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException

from ..config.config import Config
from ..locators import BasePageLocators


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.base_url = Config.BASE_URL

    '''Основные методы для ui'''
    def find(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(
            EC.presence_of_element_located(locator),
            message=f"Element not found: {locator}"
        )

    def find_elements(self,locator,time=10):
        return WebDriverWait(self.browser, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Element not found: {locator}"
        )

    def open(self, url=None):
        self.browser.get(self.base_url + (url or ''))

    # Метод для проверки корректности ссылки в поисковой строке
    def is_link_correct(self, value = None):
        try:
            if value:
                WebDriverWait(self.browser, 10).until(
                    EC.url_contains(value))
                print(f'{value.capitalize()} link is correct')
            else:
                WebDriverWait(self.browser, 10).until(
                    EC.url_contains(self.base_url))
                print('Home page link is correct')
        except TimeoutException:
            raise AssertionError(f'Current link is not {value} link')

    #Метод проверки отсутствия активной сессии пользователя
    def should_not_be_username(self):
        username = self.is_not_element_present(BasePageLocators.LOGGED_AS_TEXT)

    '''Методы для перехода по страницам сайта через панель навигации'''
    def go_to_login_page(self):
        self.find(BasePageLocators.SIGNUP_LOGIN_BUTTON).click()

    def go_to_products_page(self):
        self.find(BasePageLocators.PRODUCTS_BUTTON).click()

    def go_to_cart_page(self):
        self.find(BasePageLocators.CART_BUTTON).click()

    def go_to_home_page(self):
        self.find(BasePageLocators.HOME_BUTTON).click()

    def go_to_contact_us_page(self):
        self.find(BasePageLocators.CONTACT_US_BUTTON).click()

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

    '''Методы для алертов'''

    def is_alert_present(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.alert_is_present())
            self.browser.switch_to.alert
            return True
        except NoAlertPresentException:
            return False

    def get_alert_text(self):
        alert = self.browser.switch_to.alert
        return alert.text

    def accept_alert(self):
        assert self.is_alert_present(), "Alert is not presented"
        print("Alert is presented")
        alert = self.browser.switch_to.alert
        alert.accept()

    '''Методы работы с файлами'''

    def upload_file(self,locator,file_path=None):
        if file_path is None:
            self.find(locator).send_keys('F:/Marketplace/requirements.txt')
        else:
            self.find(locator).send_keys(file_path)

    def should_be_correct_text(self,locator,text):
        self.is_element_present(locator)
        element = self.find(locator)
        assert text == element.text, f'Text is not correct: {element.text}, should be: {text}'
        print(f'Text is correct: {element.text}')

