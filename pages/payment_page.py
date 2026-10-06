import os

import allure
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

    @allure.step('Скачивание файла с инвойсом')
    def download_invoice(self, download_dir):
        self.is_element_present(PaymentPageLocators.DOWNLOAD_INVOICE_BUTTON)
        self.find(PaymentPageLocators.DOWNLOAD_INVOICE_BUTTON).click()
        print('Download invoice button clicked')
        file_path = self.wait_for_download(download_dir)
        print(f'File downloaded: {file_path}')
        return file_path

    @allure.step("Ожидание завершения скачивания файла")
    def wait_for_download(self, download_dir, timeout=30):
        """Ожидает завершения скачивания файла"""
        import time
        end_time = time.time() + timeout
        while time.time() < end_time:
            files = os.listdir(download_dir)
            # Исключаем незавершённые файлы (.crdownload)
            completed = [f for f in files if not f.endswith('.crdownload')]
            if completed:
                return os.path.join(download_dir, completed[0])
            time.sleep(0.5)
        raise TimeoutError(f"Файл не скачался за {timeout} секунд")

    @allure.step("Проверка содержимого инвойса")
    def check_invoice_content(self, file_path, login: bool = False, total_price: int = 0):
        with open(file_path, 'r') as f:
            content = f.read()
            if login:
                first_name, last_name = DataGenerator.get_login_data('first_name', 'last_name')
            else:
                first_name, last_name = DataGenerator.get_registration_data('first_name', 'last_name')
        full_name = f'{first_name} {last_name}'
        assert f'Hi {full_name}, Your total purchase amount is {total_price}. Thank you' in content,\
            (f'Incorrect invoice content: "{content[:200]}" Should be: "Hi {full_name}, Your total purchase amount is '
             f'{total_price}. Thank you"')
        print(f'Invoice content is valid')

    @allure.step('Завершение покупки')
    def finish_purchase(self):
        self.is_element_present(PaymentPageLocators.DOWNLOAD_INVOICE_BUTTON)
        continue_button = self.find(PaymentPageLocators.DOWNLOAD_INVOICE_BUTTON)
        continue_button.click()
        print('Continue button clicked')