import allure

from locators import CheckoutPageLocators
from utils.data_generator import DataGenerator
from ..pages.cart_page import CartPage


class CheckoutPage(CartPage):
    '''Методы страницы оформления заказа'''

    @allure.step("Проверка данных доставки")
    def check_delivery_details(self):
        self.is_element_present(CheckoutPageLocators.DELIVERY_FULL_NAME)
        full_name = f'{DataGenerator.get_registration_data('title')} {DataGenerator.get_registration_data('first_name')} {DataGenerator.get_registration_data('last_name')}'
        delivery_full_name = self.find(CheckoutPageLocators.DELIVERY_FULL_NAME).text
        assert full_name == delivery_full_name, f'Incorrect name in delivery information: {delivery_full_name}, should be: {full_name}'
        print(f'Name is correct in the delivery information: {delivery_full_name}')

        self.is_element_present(CheckoutPageLocators.DELIVERY_COMPANY)
        company_name = DataGenerator.get_registration_data('company')
        delivery_company_name = self.find(CheckoutPageLocators.DELIVERY_COMPANY).text
        assert company_name == delivery_company_name, f'Incorrect company name in delivery information: {delivery_company_name}, should be: {company_name}'
        print(f'Company name is correct in the delivery information: {delivery_company_name}')

        self.is_element_present(CheckoutPageLocators.DELIVERY_ADDRESS_1)
        address_1 = DataGenerator.get_registration_data('address_1')
        delivery_address_1 = self.find(CheckoutPageLocators.DELIVERY_ADDRESS_1).text
        assert address_1 == delivery_address_1, f'Incorrect address 1 in delivery information: {delivery_address_1}, should be: {address_1}'
        print(f'Address 1 is correct in the delivery information: {delivery_address_1}')

        self.is_element_present(CheckoutPageLocators.DELIVERY_ADDRESS_2)
        address_2 = DataGenerator.get_registration_data('address_2')
        delivery_address_2 = self.find(CheckoutPageLocators.DELIVERY_ADDRESS_2).text
        assert address_2 == delivery_address_2, f'Incorrect address 2 in delivery information: {delivery_address_2}, should be: {address_2}'
        print(f'Address 2 is correct in the delivery information: {delivery_address_2}')

        self.is_element_present(CheckoutPageLocators.DELIVERY_CITY_STATE_AND_CODE)
        city_state_and_code = f'{DataGenerator.get_registration_data('city')} {DataGenerator.get_registration_data('state')} {DataGenerator.get_registration_data('zipcode')}'
        delivery_city_state_and_code = self.find(CheckoutPageLocators.DELIVERY_CITY_STATE_AND_CODE).text
        assert city_state_and_code == delivery_city_state_and_code, f'Incorrect city in delivery information: {delivery_city_state_and_code}, should be: {city_state_and_code}'
        print(f'City is correct in the delivery information: {delivery_city_state_and_code}')

        self.is_element_present(CheckoutPageLocators.DELIVERY_COUNTRY)
        country = DataGenerator.get_registration_data('country')
        delivery_country = self.find(CheckoutPageLocators.DELIVERY_COUNTRY).text
        assert country == delivery_country, f'Incorrect country in delivery information: {delivery_country}, should be: {country}'
        print(f'Country is correct in the delivery information: {delivery_country}')

        self.is_element_present(CheckoutPageLocators.DELIVERY_PHONE)
        phone = DataGenerator.get_registration_data('mobile_number')
        delivery_phone = self.find(CheckoutPageLocators.DELIVERY_PHONE).text
        assert phone == delivery_phone, f'Incorrect phone in delivery information: {delivery_phone}, should be: {phone}'
        print(f'Phone is correct in the delivery information: {delivery_phone}')

    @allure.step("Проверка данных для счетов")
    def check_billing_details(self):
        self.is_element_present(CheckoutPageLocators.BILLING_FULL_NAME)
        full_name = f'{DataGenerator.get_registration_data('title')} {DataGenerator.get_registration_data('first_name')} {DataGenerator.get_registration_data('last_name')}'
        billing_full_name = self.find(CheckoutPageLocators.BILLING_FULL_NAME).text
        assert full_name == billing_full_name, f'Incorrect name in billing information: {billing_full_name}, should be: {full_name}'
        print(f'Name is correct in the billing information: {billing_full_name}')

        self.is_element_present(CheckoutPageLocators.BILLING_COMPANY)
        company_name = DataGenerator.get_registration_data('company')
        billing_company_name = self.find(CheckoutPageLocators.BILLING_COMPANY).text
        assert company_name == billing_company_name, f'Incorrect company name in billing information: {billing_company_name}, should be: {company_name}'
        print(f'Company name is correct in the billing information: {billing_company_name}')

        self.is_element_present(CheckoutPageLocators.BILLING_ADDRESS_1)
        address_1 = DataGenerator.get_registration_data('address_1')
        billing_address_1 = self.find(CheckoutPageLocators.BILLING_ADDRESS_1).text
        assert address_1 == billing_address_1, f'Incorrect address 1 in billing information: {billing_address_1}, should be: {address_1}'
        print(f'Address 1 is correct in the billing information: {billing_address_1}')

        self.is_element_present(CheckoutPageLocators.BILLING_ADDRESS_2)
        address_2 = DataGenerator.get_registration_data('address_2')
        billing_address_2 = self.find(CheckoutPageLocators.BILLING_ADDRESS_2).text
        assert address_2 == billing_address_2, f'Incorrect address 2 in billing information: {billing_address_2}, should be: {address_2}'
        print(f'Address 2 is correct in the billing information: {billing_address_2}')

        self.is_element_present(CheckoutPageLocators.BILLING_CITY_STATE_AND_CODE)
        city_state_and_code = f'{DataGenerator.get_registration_data('city')} {DataGenerator.get_registration_data('state')} {DataGenerator.get_registration_data('zipcode')}'
        billing_city_state_and_code = self.find(CheckoutPageLocators.BILLING_CITY_STATE_AND_CODE).text
        assert city_state_and_code == billing_city_state_and_code, f'Incorrect city in billing information: {billing_city_state_and_code}, should be: {city_state_and_code}'
        print(f'City is correct in the billing information: {billing_city_state_and_code}')

        self.is_element_present(CheckoutPageLocators.BILLING_COUNTRY)
        country = DataGenerator.get_registration_data('country')
        billing_country = self.find(CheckoutPageLocators.BILLING_COUNTRY).text
        assert country == billing_country, f'Incorrect country in billing information: {billing_country}, should be: {country}'
        print(f'Country is correct in the billing information: {billing_country}')

        self.is_element_present(CheckoutPageLocators.BILLING_PHONE)
        phone = DataGenerator.get_registration_data('mobile_number')
        billing_phone = self.find(CheckoutPageLocators.BILLING_PHONE).text
        assert phone == billing_phone, f'Incorrect phone in billing information: {billing_phone}, should be: {phone}'
        print(f'Phone is correct in the billing information: {billing_phone}')

    @allure.step("Заполнение комментария к заказу")
    def fill_comment(self):
        comment_field = CheckoutPageLocators.COMMENT_FIELD
        message = DataGenerator.get_message()
        self.is_element_present(comment_field)
        self.find(comment_field).send_keys(message)
        print(f'Comment filled in with: {message}')

    @allure.step("Переход на страницу оплаты")
    def place_order(self):
        self.is_element_present(CheckoutPageLocators.PLACE_ORDER_BUTTON)
        self.find(CheckoutPageLocators.PLACE_ORDER_BUTTON).click()
        print('Place order button clicked')
        self.is_link_correct('/payment')

