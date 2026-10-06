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

    @allure.step("Прокрутка до элемента")
    def scroll_to_element(self, locator):
        self.is_element_present(locator)
        self.browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            self.find(locator)
        )

    @allure.step("Проверка имени пользователя")
    def check_username(self, login=False):
        '''Проверка корректности отображения
        авторизованного пользователя в панели навигации'''
        if login:
            expected_name = DataGenerator.get_login_data('first_name')
        else:
            expected_name = DataGenerator.get_registration_data('first_name')
        logged_as = self.find(BasePageLocators.LOGGED_AS_TEXT).text
        assert f'Logged in as {expected_name}' in logged_as, f'Logged in text is incorrect {logged_as}'
        print(f'Username is correct {logged_as}')

    @allure.step("Удаление аккаунта")
    def delete_account(self):
        # Проверка корректности отображения информации при удалении пользователя
        self.find(BasePageLocators.DELETE_ACCOUNT_BUTTON).click()
        title = self.find(BasePageLocators.DELETE_TITLE).text
        message_1 = self.find(BasePageLocators.DELETE_TEXT_1).text
        message_2 = self.find(BasePageLocators.DELETE_TEXT_2).text
        continue_button = self.find(BasePageLocators.DELETE_CONTINUE_BUTTON)
        assert 'ACCOUNT DELETED!' in title, f'Delete title is incorrect {title}'
        print(f'Delete title is correct {title}')
        assert 'Your account has been permanently deleted!' in message_1, f'Delete message 1 is incorrect {message_1}'
        print(f'Delete message 1 is correct {message_1}')
        assert 'You can create new account to take advantage of member privileges to enhance your online shopping experience with us.' in message_2, \
            f'Delete message 2 is incorrect {message_2}'
        print(f'Delete message 2 is correct {message_2}')
        continue_button.click()
        print('Continue button clicked')

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.find(BasePageLocators.LOGOUT_BUTTON).click()
        self.is_link_correct('login')
        self.is_not_element_present(BasePageLocators.LOGOUT_BUTTON)
        self.is_not_element_present(BasePageLocators.DELETE_ACCOUNT_BUTTON)

    @allure.step("Проверка видимости элемента в области экрана")
    def is_element_in_viewport(self, locator):
        element = self.find(locator)
        in_viewport = self.browser.execute_script("""
            var rect = arguments[0].getBoundingClientRect();
            return (
                rect.top >= 0 &&
                rect.left >= 0 &&
                rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                rect.right <= (window.innerWidth || document.documentElement.clientWidth)
            );
        """, element)
        assert in_viewport, f"Element {locator} is not in viewport"
        print(f'Element {locator} is in viewport')

    @allure.step("Скроллинг до низа страницы")
    def scroll_to_the_bottom(self):
        subscription_title = BasePageLocators.SUBSCRIPTION
        self.is_element_present(subscription_title)
        self.scroll_to_element(subscription_title)
        self.is_element_in_viewport(subscription_title)
        print('Page scrolled down')

    @allure.step("Скроллинг до верха страницы с помощью кнопки прокрутки")
    def scroll_to_the_top_by_angle(self):
        self.is_element_present(BasePageLocators.ANGLE_UP)
        angle_up = self.find(BasePageLocators.ANGLE_UP)
        angle_up.click()
        try:
            self.is_element_in_viewport(BasePageLocators.TOP_TITLE)
        except AssertionError:
            self.is_element_in_viewport(BasePageLocators.TOP_TITLE)
        print('Page scrolled up with angle up')

    @allure.step("Скроллинг до верха страницы")
    def scroll_to_the_top(self):
        top_title = BasePageLocators.TOP_TITLE
        self.is_element_present(top_title)
        self.scroll_to_element(top_title)
        try:
            self.is_element_in_viewport(BasePageLocators.TOP_TITLE)
        except AssertionError:
            self.is_element_in_viewport(BasePageLocators.TOP_TITLE)
        print('Page scrolled up with angle up')

    @allure.step("Проверка кнопки Contact Us")
    def should_be_contact_us_button(self):
        assert self.is_element_present(BasePageLocators.CONTACT_US_BUTTON), 'Contact us button is not presented'
        print('Contact us button is presented')
