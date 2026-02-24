from .base_page import BasePage
from ..locators import LoginPageLocators
from ..utils.data_generator import DataGenerator

class LoginPage(BasePage):
    
    def should_be_login_url(self) -> None:
        # Проверка корректности ссылки страницы авторизации и регистрации
        assert "login" in self.driver.current_url, 'Current link is not login link'
        print('Login link is correct')
    
    def should_be_login_fields(self):
        # Проверка наличия полей для авторизации
        assert self.is_element_present(LoginPageLocators.EMAIL_LOGIN_FIELD), 'Login email area is not presented'
        print('Login email area is presented')
        assert self.is_element_present(LoginPageLocators.PASSWORD_LOGIN_FIELD),'Password area is not presented'
        print('Password area is presented')
    
    def should_be_signup_fields(self):
        # Проверка наличия полей для регистрации
        assert self.is_element_present(LoginPageLocators.EMAIL_SIGN_UP_FIELD), 'Signup email area is not presented'
        print('Signup email area is presented')
        assert self.is_element_present(LoginPageLocators.NAME_SIGN_UP_FIELD), 'Signup name area is not presented'
        print('Signup name area is not presented')
    
    def fill_signup_fields(self):
        # Заполнение полей для регистрации
        email = DataGenerator.get_registration_data('email')
        self.find(LoginPageLocators.EMAIL_SIGN_UP_FIELD).send_keys(email)
        print('Email signup field filled')
        name = DataGenerator.get_registration_data('first_name')
        self.find(LoginPageLocators.NAME_SIGN_UP_FIELD).send_keys(name)
        print('Name signup field filled')
        
    def click_signup_button(self):
        # Переход на основную страницу регистрации
        self.find(LoginPageLocators.SIGN_UP_BUTTON).click()
        print('Signup button is clicked')
    
    def should_be_new_user_text(self):
        # Проверка сообщений об успешной регистрации
        assert self.is_element_present(LoginPageLocators.NEW_USER_TITLE), 'New user Signup title is not presented'
        print('New user Signup title is presented')
        assert 'New User Signup!' in self.find(LoginPageLocators.NEW_USER_TITLE).text, f'New user Signup title text is not correct {self.find(LoginPageLocators.NEW_USER_TITLE).text}'
        print('New user Signup title text is correct')
        

    