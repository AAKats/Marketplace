from ..utils.data_generator import DataGenerator

from ..locators import BasePageLocators
from ..pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, *args, **kwargs):
        super(HomePage, self).__init__(*args, **kwargs)

    def check_username(self,login = False):
        '''Проверка корректности отображения
        авторизованного пользователя в панели навигации'''
        if login:
            expected_name = DataGenerator.get_login_data('first_name')
        else:
            expected_name = DataGenerator.get_registration_data('first_name')
        logged_as = self.find(BasePageLocators.LOGGED_AS_TEXT).text
        assert f'Logged in as {expected_name}' in logged_as, f'Logged in text is incorrect {logged_as}'
        print(f'Username is correct {logged_as}')

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

    def logout(self):
        self.find(BasePageLocators.LOGOUT_BUTTON).click()
        self.is_link_correct('login')
        self.is_not_element_present(BasePageLocators.LOGOUT_BUTTON)
        self.is_not_element_present(BasePageLocators.DELETE_ACCOUNT_BUTTON)

    def should_be_contact_us_button(self):
        assert self.is_element_present(BasePageLocators.CONTACT_US_BUTTON), 'Contact us button is not presented'
        print('Contact us button is presented')


