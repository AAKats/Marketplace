import allure
from .base_page import BasePage
from .home_page import HomePage
from ..locators import LoginPageLocators
from ..utils.data_generator import DataGenerator

class LoginPage(BasePage):

    @allure.step("Проверка полей авторизации")
    def should_be_login_fields(self):
        assert self.is_element_present(LoginPageLocators.EMAIL_LOGIN_FIELD), 'Login email area is not presented'
        print('Login email area is presented')
        assert self.is_element_present(LoginPageLocators.PASSWORD_LOGIN_FIELD),'Password area is not presented'
        print('Password area is presented')
    
    @allure.step("Проверка полей регистрации")
    def should_be_signup_fields(self):
        assert self.is_element_present(LoginPageLocators.EMAIL_SIGN_UP_FIELD), 'Signup email area is not presented'
        print('Signup email area is presented')
        assert self.is_element_present(LoginPageLocators.NAME_SIGN_UP_FIELD), 'Signup name area is not presented'
        print('Signup name area is not presented')
    
    @allure.step("Заполнение email для регистрации")
    def fill_signup_email(self):
        email = DataGenerator.get_registration_data('email')
        self.find(LoginPageLocators.EMAIL_SIGN_UP_FIELD).send_keys(email)
        print('Email signup field filled')

    @allure.step("Заполнение имени для регистрации")
    def fill_signup_name(self):
        try:
            name = DataGenerator.get_registration_data('first_name')
        except:
            name = 'Bob'
        self.find(LoginPageLocators.NAME_SIGN_UP_FIELD).send_keys(name)
        print('Name signup field filled')
        
    @allure.step("Нажатие кнопки регистрации")
    def click_signup_button(self):
        self.find(LoginPageLocators.SIGN_UP_BUTTON).click()
        print('Signup button is clicked')
    
    @allure.step("Проверка заголовка New User")
    def should_be_new_user_text(self):
        assert self.is_element_present(LoginPageLocators.NEW_USER_TITLE), 'New user Signup title is not presented'
        print('New user Signup title is presented')
        assert 'New User Signup!' in self.find(LoginPageLocators.NEW_USER_TITLE).text, f'New user Signup title text is not correct {self.find(LoginPageLocators.NEW_USER_TITLE).text}'
        print('New user Signup title text is correct')
        
    @allure.step("Проверка заголовка Login")
    def should_be_correct_login_title(self):
        assert self.is_element_present(LoginPageLocators.LOGIN_TITLE), 'Login title is not presented'
        print('Login title is presented')
        assert 'Login to your account' in self.find(LoginPageLocators.LOGIN_TITLE).text, f'Login title text is not correct {self.find(LoginPageLocators.LOGIN_TITLE).text}'
        print('Login title text is correct')

    @allure.step("Заполнение email")
    def fill_in_email(self, email= None):
        if email != None:
            self.find(LoginPageLocators.EMAIL_LOGIN_FIELD).send_keys(email)
            print('Email filled in')
        else:
            email = DataGenerator.get_login_data('email')
            self.find(LoginPageLocators.EMAIL_LOGIN_FIELD).send_keys(email)
            print('Email filled in')
    
    @allure.step("Заполнение пароля")
    def fill_in_password(self):
        password = DataGenerator.get_login_data('password')
        self.find(LoginPageLocators.PASSWORD_LOGIN_FIELD).send_keys(password)
        print('Password filled in')

    @allure.step("Нажатие кнопки входа")
    def click_login_button(self):
        assert self.is_element_present(LoginPageLocators.LOGIN_BUTTON),'Login button is not presented'
        print('Login button is presented')
        self.find(LoginPageLocators.LOGIN_BUTTON).click()
        print('Login button is clicked')

    @allure.step("Проверка ошибки входа")
    def should_be_correct_login_error_message(self):
        self.is_element_present(LoginPageLocators.LOGIN_ERROR)
        print('Error is presented')
        error_message = self.find(LoginPageLocators.LOGIN_ERROR).text
        assert 'Your email or password is incorrect!' in error_message, f'Error message should be "Your email or password is incorrect!" got {error_message}'
        print(f'Error message is correct: {error_message}')

    @allure.step("Проверка ошибки регистрации")
    def should_be_correct_signup_error_message(self):
        self.is_element_present(LoginPageLocators.SIGN_UP_ERROR)
        print('Error is presented')
        error_message = self.find(LoginPageLocators.SIGN_UP_ERROR).text
        assert 'Email Address already exist!' in error_message, f'Error message should be "Email Address already exist!" got {error_message}'
        print(f'Error message is correct: {error_message}')

    @allure.step("Заполнение существующего email")
    def fill_in_existing_email(self, email= None):
        if email != None:
            self.find(LoginPageLocators.EMAIL_SIGN_UP_FIELD).send_keys(email)
            print('Email filled in')
        else:
            email = DataGenerator.get_login_data('email')
            self.find(LoginPageLocators.EMAIL_SIGN_UP_FIELD).send_keys(email)
            print('Existing email filled in')
