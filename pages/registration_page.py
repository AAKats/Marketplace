from typing import Literal

import allure
from ..utils.data_generator import DataGenerator

from ..pages.base_page import BasePage
from ..locators import RegistrationPageLocators

class RegistrationPage(BasePage):

    @allure.step("Проверка URL регистрации")
    def should_be_signup_url(self) -> None:
        self.is_link_correct('signup')

    
    @allure.step("Проверка заголовка Account Information")
    def should_be_account_information_text(self):
        # Проверка корректности заголовка основной информации при регистрации
        assert self.is_element_present(RegistrationPageLocators.ACCOUNT_INFORMATION_TITLE), 'Account information title is not presented'
        print('Account information title is not presented')
        assert 'ENTER ACCOUNT INFORMATION' in self.find(RegistrationPageLocators.ACCOUNT_INFORMATION_TITLE).text,\
              f'Account information title text is not correct {self.find(RegistrationPageLocators.ACCOUNT_INFORMATION_TITLE).text}'
        print('Account information title text is correct')

    @allure.step("Выбор пола")
    def select_sex_checkbox(self, autogen = False, sex: Literal["f - female", "m - male"] | None = None):
        # Выбор пола при регистрации, доступны выбор из сгенерированного файла или по указанному ключу
        assert self.is_element_present(RegistrationPageLocators.MR_RADIOBUTTON), 'Mr radiobutton is not presented'
        print('Mr radiobutton is presented')
        assert self.is_element_present(RegistrationPageLocators.MRS_RADIOBUTTON), 'Mrs radiobutton is not presented'
        print('Mrs radiobutton is presented')
        if autogen:
            sex = DataGenerator.get_registration_data('title')
        if sex == 'Mr.' or sex == 'm':
            self.find(RegistrationPageLocators.MR_RADIOBUTTON).click()
            print('Selected MR title')
        elif sex == 'Mrs.' or sex == 'f':
            self.find(RegistrationPageLocators.MRS_RADIOBUTTON).click()
            print('Selected MRS title')

    '''Методы для проверки введенной информации в окне авторизации и регистрации'''
    @allure.step("Проверка поля email")
    def check_email_field(self):
        expected_email = DataGenerator.get_registration_data('email')
        fact_email = self.find(RegistrationPageLocators.EMAIL_FIELD).get_attribute('value')
        assert expected_email in fact_email, f'Email is not correct {fact_email} not equal expected {expected_email}'

    @allure.step("Проверка поля имени")
    def check_name_field(self):
        expected_name = DataGenerator.get_registration_data('first_name')
        fact_name = self.find(RegistrationPageLocators.NAME_FIELD).get_attribute('value')
        assert expected_name in fact_name, f'Name is not correct {fact_name} not equal expected {expected_name}'

    '''Методы для заполнения основных полей страницы регистрации'''
    @allure.step("Заполнение пароля")
    def fill_in_password(self):
        password = DataGenerator.get_registration_data('password')
        assert self.is_element_present(RegistrationPageLocators.PASSWORD_FIELD),'Password field is not presented'
        print('Password field is presented')
        self.find(RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
        print('Password is filled in')

    @allure.step("Заполнение даты рождения")
    def fill_in_date_of_birth(self):
        assert self.is_element_present(RegistrationPageLocators.DAY_OF_BIRTH_LIST), 'Day of birth list is not presented'
        print('Day of birth list is presented')
        day_of_birth = DataGenerator.get_registration_data('day_of_birth')
        self.select_by_value(RegistrationPageLocators.DAY_OF_BIRTH_LIST,day_of_birth)
        print('Day of birth selected')

        assert self.is_element_present(RegistrationPageLocators.MONTH_OF_BIRTH_LIST), 'Month of birth list is not presented'
        print('Month of birth list is presented')
        month_of_birth = DataGenerator.get_registration_data('month_of_birth')
        self.select_by_value(RegistrationPageLocators.MONTH_OF_BIRTH_LIST,month_of_birth)
        print('Month of birth selected')

        assert self.is_element_present(RegistrationPageLocators.YEAR_OF_BIRTH_LIST), 'Year of birth list is not presented'
        print('Year of birth list is presented')
        year_of_birth = DataGenerator.get_registration_data('year_of_birth')
        self.select_by_value(RegistrationPageLocators.YEAR_OF_BIRTH_LIST,year_of_birth)
        print('Year of birth selected')

    @allure.step("Выбор подписки на новости")
    def select_newsletter_checkbox(self,should_be_random = False, select= False):
        # Выбор подписки на новости, рандомный из сгенерированных данных или указать select
        newsletter = DataGenerator.get_registration_data('newsletter')
        if should_be_random and not select:
            if newsletter == True:
                self.find(RegistrationPageLocators.NEWSLETTER_CHECKBOX).click()
                print('Sign up for our newsletter! checkbox is selected')
            else:
                print('Sign up for our newsletter! checkbox is not selected')
        elif not should_be_random and select:
            self.find(RegistrationPageLocators.NEWSLETTER_CHECKBOX).click()
            print('Sign up for our newsletter! checkbox is selected')
        else:
            print('Sign up for our newsletter! checkbox is not selected')

    @allure.step("Выбор подписки на спецпредложения")
    def select_special_offers_checkbox(self,should_be_random = False, select= False):
        special_offers = DataGenerator.get_registration_data('offers')
        # Выбор подписки на спецпредложения, рандомный из сгенерированных данных или указать select
        if should_be_random and not select:
            if special_offers == True:
                self.find(RegistrationPageLocators.OFFERS_CHECKBOX).click()
                print('Receive special offers from our partners! checkbox is selected')
            else:
                print('Receive special offers from our partners! checkbox is not selected')
        elif not should_be_random and select:
            self.find(RegistrationPageLocators.OFFERS_CHECKBOX).click()
            print('Receive special offers from our partners! checkbox is selected')
        else:
            print('Receive special offers from our partners! checkbox is not selected')

    @allure.step("Заполнение имени")
    def fill_in_first_name(self):
        first_name = DataGenerator.get_registration_data('first_name')
        assert self.is_element_present(RegistrationPageLocators.FIRST_NAME_FIELD),'First name field is not presented'
        print('First name field is presented')
        self.find(RegistrationPageLocators.FIRST_NAME_FIELD).send_keys(first_name)
        print('First name is filled in')
    
    @allure.step("Заполнение фамилии")
    def fill_in_last_name(self):
        last_name = DataGenerator.get_registration_data('last_name')
        assert self.is_element_present(RegistrationPageLocators.LAST_NAME_FIELD),'Last name field is not presented'
        print('Last name field is presented')
        self.find(RegistrationPageLocators.LAST_NAME_FIELD).send_keys(last_name)
        print('Last name is filled in')

    @allure.step("Заполнение компании")
    def fill_in_company(self):
        company = DataGenerator.get_registration_data('company')
        assert self.is_element_present(RegistrationPageLocators.COMPANY_FIELD),'Company field is not presented'
        print('Company field is presented')
        self.find(RegistrationPageLocators.COMPANY_FIELD).send_keys(company)
        print('Company is filled in')

    @allure.step("Заполнение адреса (строка 1)")
    def fill_in_address_1(self):
        address_1 = DataGenerator.get_registration_data('address_1')
        assert self.is_element_present(RegistrationPageLocators.ADDRESS_FIELD),'Address 1 field is not presented'
        print('Address 1 field is presented')
        self.find(RegistrationPageLocators.ADDRESS_FIELD).send_keys(address_1)
        print('Address 1 is filled in')

    @allure.step("Заполнение адреса (строка 2)")
    def fill_in_address_2(self):
        address_2 = DataGenerator.get_registration_data('address_2')
        assert self.is_element_present(RegistrationPageLocators.ADDRESS_2_FIELD),'Address 2 field is not presented'
        print('Address 2 field is presented')
        self.find(RegistrationPageLocators.ADDRESS_2_FIELD).send_keys(address_2)
        print('Address 2 is filled in')

    @allure.step("Заполнение города")
    def fill_in_city(self):
        city = DataGenerator.get_registration_data('city')
        assert self.is_element_present(RegistrationPageLocators.CITY_FIELD),'City field is not presented'
        print('City field is presented')
        self.find(RegistrationPageLocators.CITY_FIELD).send_keys(city)
        print('City is filled in')

    @allure.step("Заполнение штата")
    def fill_in_state(self):
        state = DataGenerator.get_registration_data('state')
        assert self.is_element_present(RegistrationPageLocators.STATE_FIELD),'State field is not presented'
        print('State field is presented')
        self.find(RegistrationPageLocators.STATE_FIELD).send_keys(state)
        print('State is filled in')

    @allure.step("Выбор страны")
    def select_country(self, country_name = None):
        # Выбор страны, рандомный из сгенерированных данных или указать название
        country = DataGenerator.get_registration_data('country')
        if country_name == None:
            self.select_by_value(RegistrationPageLocators.COUTNRY_LIST,country)
        else:
            self.select_by_value(RegistrationPageLocators.COUTNRY_LIST,country_name)

    @allure.step("Заполнение индекса")
    def fill_in_zipcode(self):
        zipcode = DataGenerator.get_registration_data('zipcode')
        assert self.is_element_present(RegistrationPageLocators.ZIPCODE_FIELD),'Zipcode field is not presented'
        print('Zipcode field is presented')
        self.find(RegistrationPageLocators.ZIPCODE_FIELD).send_keys(zipcode)
        print('Zipcode is filled in')
    
    @allure.step("Заполнение телефона")
    def fill_in_mobile_number(self):
        mobile_number = DataGenerator.get_registration_data('mobile_number')
        assert self.is_element_present(RegistrationPageLocators.MOBILE_NUMBER_FIELD),'Mobile number field is not presented'
        print('Mobile number field is presented')
        self.find(RegistrationPageLocators.MOBILE_NUMBER_FIELD).send_keys(mobile_number)
        print('Mobile number is filled in')

    @allure.step("Завершение создания аккаунта")
    def finish_account_creation(self):
        self.find(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()
        self.is_link_correct('account_created')

    '''Методы для проверки завершающего этапа регистрации'''
    @allure.step("Проверка заголовка Account Created")
    def should_be_correct_title(self):
        title = self.find(RegistrationPageLocators.ACCOUNT_CREATED_TITLE).text
        assert 'ACCOUNT CREATED!' in title, f'Account Created! title is incorrect: {title}'
        print(f'Title is correct {title}')

    @allure.step("Проверка сообщения об успехе")
    def should_be_correct_congratilations(self):
        congratilations_text_1 = self.find(RegistrationPageLocators.CONGRATILATIONS_TEXT).text
        congratilations_text_2 = self.find(RegistrationPageLocators.CONGRATILATIONS_TEXT_2).text
        assert 'Congratulations! Your new account has been successfully created!' in congratilations_text_1, f'Congratilations text 1 is incorrect: {congratilations_text_1}'
        print(f'Congratilations text 1 is correct: {congratilations_text_1}')
        assert 'You can now take advantage of member privileges to enhance your online shopping experience with us.' in congratilations_text_2,f'Congratilations text 2 is incorrect: {congratilations_text_2}'
        print(f'Congratilations text 2 is correct: {congratilations_text_2}')

    @allure.step("Завершение регистрации")
    def finish_signup(self):
        assert self.is_element_present(RegistrationPageLocators.CONTINUE_AFTER_SIGNUP_BUTTON), 'Continue button is not presented'
        print('Continue button is presented')
        self.find(RegistrationPageLocators.CONTINUE_AFTER_SIGNUP_BUTTON).click()


