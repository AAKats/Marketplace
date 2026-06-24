import allure
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.data_generator import DataGenerator
from ..locators import PaymentPageLocators
from ..pages.base_page import BasePage


class PaymentPage(BasePage):
    '''Методы для страницы оплаты'''

    @allure.step("Заполнение данных карты для оплаты")
    def fill_in_card_info(self):
        DataGenerator.generate_card_info()
        name_on_card_field = PaymentPageLocators.NAME_ON_CARD
        name_on_card = DataGenerator.get_card_info('name_on_card')
        self.is_element_present(name_on_card_field)
        self.find(name_on_card_field).send_keys(name_on_card)
        print(f'Name on card filled in with: {name_on_card}')

        card_number_field = PaymentPageLocators.CARD_NUMBER
        card_number = DataGenerator.get_card_info('card_number')
        self.is_element_present(card_number_field)
        self.find(card_number_field).send_keys(card_number)
        print(f'Card number filled in with: {card_number}')

        cvc_field = PaymentPageLocators.CVC
        cvc = DataGenerator.get_card_info('cvc')
        self.is_element_present(cvc_field)
        self.find(cvc_field).send_keys(cvc)
        print(f'CVC filled in with: {cvc}')

        expiry_m_field = PaymentPageLocators.EXPIRATION_M
        expiry_m = DataGenerator.get_card_info('expiration_m')
        self.is_element_present(expiry_m_field)
        self.find(expiry_m_field).send_keys(expiry_m)
        print(f'Expiry month filled in with: {expiry_m}')

        expiry_y_field = PaymentPageLocators.EXPIRATION_Y
        expiry_y = DataGenerator.get_card_info('expiration_y')
        self.is_element_present(expiry_y_field)
        self.find(expiry_y_field).send_keys(expiry_y)
        print(f'Expiry year filled in with: {expiry_y}')

    @allure.step("Оплата и подтверждение заказа")
    def pay_and_confirm(self):
        self.is_element_present(PaymentPageLocators.PAY_AND_CONFIRM_BUTTON)
        self.find(PaymentPageLocators.PAY_AND_CONFIRM_BUTTON).click()
        print('Pay and confirm button clicked')

    @allure.step('Проверка корректности сообщения об успешной оплате')
    def should_be_correct_payment_success_message(self):
        self.browser.back()
        self.is_element_present(PaymentPageLocators.SUCCESS_MESSAGE)
        self.is_element_visible(PaymentPageLocators.SUCCESS_MESSAGE)
        assert 'Your order has been placed successfully!' in self.find(PaymentPageLocators.SUCCESS_MESSAGE).text, f'Incorrect success message: "{self.find(PaymentPageLocators.SUCCESS_MESSAGE).text}", should be "Your order has been placed successfully!"'
        print(f'Success message is correct: "{self.find(PaymentPageLocators.SUCCESS_MESSAGE).text}"')
        self.browser.forward()