import os

import allure
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException, \
    ElementNotInteractableException

from utils.data_generator import DataGenerator
from ..config.config import Config
from ..locators import BasePageLocators, ProductsPageLocators


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.base_url = Config.BASE_URL

    '''Основные методы для ui'''
    @allure.step("Поиск элемента {locator}")
    def find(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(
            EC.presence_of_element_located(locator),
            message=f"Element not found: {locator}"
        )

    @allure.step("Поиск всех элементов {locator}")
    def find_elements(self,locator,time=10):
        return WebDriverWait(self.browser, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Element not found: {locator}"
        )

    @allure.step("Открыть страницу")
    def open(self, url=None):
        self.browser.get(self.base_url + (url or ''))

    # Метод для проверки корректности ссылки в поисковой строке
    @allure.step("Проверка URL")
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
    @allure.step("Проверка отсутствия авторизации")
    def should_not_be_username(self):
        username = self.is_not_element_present(BasePageLocators.LOGGED_AS_TEXT)

    '''Методы для перехода по страницам сайта через панель навигации'''
    @allure.step("Переход на страницу входа")
    def go_to_login_page(self):
        self.find(BasePageLocators.SIGNUP_LOGIN_BUTTON).click()

    @allure.step("Переход на страницу товаров")
    def go_to_products_page(self):
        self.find(BasePageLocators.PRODUCTS_BUTTON).click()

    @allure.step("Переход в корзину")
    def go_to_cart_page(self):
        self.find(BasePageLocators.CART_BUTTON).click()

    @allure.step("Переход на главную")
    def go_to_home_page(self):
        self.find(BasePageLocators.HOME_BUTTON).click()

    @allure.step("Переход на страницу контактов")
    def go_to_contact_us_page(self):
        self.find(BasePageLocators.CONTACT_US_BUTTON).click()

    '''Методы для проверки наличия или отсутствия элемента на странице'''
    @allure.step("Проверка наличия элемента")
    def is_element_present(self, locator):
        try:
            self.find(locator)
        except (NoSuchElementException, TimeoutException):
            return False
        return True

    @allure.step("Проверка отсутствия элемента")
    def is_not_element_present(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((locator)))
        except TimeoutException:
            return True
        return False
    
    '''Методы для выпадающих списков'''
    @allure.step("Выбор значения из списка")
    def select_by_value(self, locator, value):
        try:
            Select(self.find(locator)).select_by_value(value)
        except NoSuchElementException as element:
            print(f"Элемент не найден в выпадающем списке: {element}")

    '''Методы для алертов'''

    @allure.step("Проверка наличия алерта")
    def is_alert_present(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.alert_is_present())
            self.browser.switch_to.alert
            return True
        except NoAlertPresentException:
            return False

    @allure.step("Получение текста алерта")
    def get_alert_text(self):
        alert = self.browser.switch_to.alert
        return alert.text

    @allure.step("Принятие алерта")
    def accept_alert(self):
        assert self.is_alert_present(), "Alert is not presented"
        print("Alert is presented")
        alert = self.browser.switch_to.alert
        alert.accept()

    '''Методы работы с файлами'''

    @allure.step("Загрузка файла")
    def upload_file(self,locator,file_path=None):
        if file_path is None:
            path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'requirements.txt')
            self.find(locator).send_keys(path)
        else:
            self.find(locator).send_keys(file_path)

    @allure.step("Проверка текста элемента")
    def should_be_correct_text(self,locator,text):
        self.is_element_present(locator)
        element = self.find(locator)
        assert text == element.text, f'Text is not correct: {element.text}, should be: {text}'
        print(f'Text is correct: {element.text}')

    @allure.step("Проверка текста подписки")
    def should_be_correct_subscription_text(self):
        self.should_be_correct_text(BasePageLocators.SUBSCRIPTION,'SUBSCRIPTION')

    @allure.step("Ввод email для подписки")
    def input_subscribe_email(self):
        email_form = BasePageLocators.SUBSCRIBE_EMAIL_FORM
        email = DataGenerator.get_login_data('email')
        self.is_element_present(email_form)
        self.find(email_form).send_keys(email)
        print(f'Email filled in with "{email}"')

    @allure.step("Нажатие кнопки подписки")
    def click_subscribe(self):
        button = BasePageLocators.SUBSCRIBE_BUTTON
        self.is_element_present(button)
        self.find(button).click()
        print('Subscribe button is clicked')

    @allure.step("Проверка успешной подписки")
    def should_be_success_subscribe_alert(self):
        alert = BasePageLocators.SUCCESS_SUBSCRIBE_ALERT
        self.is_element_present(alert)
        self.should_be_correct_text(alert,'You have been successfully subscribed!')

    @allure.step("Проверка кликабельности элемента")
    def is_element_clickable(self,locator):
        """ Проверяет кликабельность элемента.
        Работает только с локатором
        """
        try:
            WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(locator))
            return True
        except ElementNotInteractableException:
            return False

    @allure.step("Проверка видимости элемента")
    def is_element_visible(self, element, timeout=5):
        """Ожидает видимости элемента.
        Принимает как locator (tuple), так и WebElement.
        """
        try:
            if isinstance(element, tuple):
                return WebDriverWait(self.browser, timeout).until(
                    EC.visibility_of_element_located(element)
                )
            return WebDriverWait(self.browser, timeout).until(
                EC.visibility_of(element)
            )
        except TimeoutException:
            raise AssertionError(f"Element not visible after {timeout}s: {element}")

    @allure.step("Переход в корзину через модальное окно")
    def go_to_cart_via_modal(self):
        self.is_element_visible(ProductsPageLocators.VIEW_CART_VIA_MODAL)
        self.find(ProductsPageLocators.VIEW_CART_VIA_MODAL).click()
