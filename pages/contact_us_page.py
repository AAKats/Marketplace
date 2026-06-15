import allure

from locators import ContactUsPageLocators
from ..utils.data_generator import DataGenerator

from ..locators import BasePageLocators
from ..pages.base_page import BasePage

class ContactUsPage(BasePage):
    '''Методы страницы обратной связи'''

    @allure.step("Проверка заголовка Contact Us")
    def should_be_correct_title(self):
        main_title = ContactUsPageLocators.CONTACT_US_TITLE
        assert self.is_element_present(main_title), 'Main title is not presented'
        print('Main title is presented')
        assert 'CONTACT US' in self.find(main_title).text, f'Main title should be: "CONTACT US" got: {self.find(main_title).text}'
        print(f'Main title is correct: {self.find(main_title).text}')

    @allure.step("Проверка второго заголовка")
    def should_be_correct_second_title(self):
        second_title = ContactUsPageLocators.CONTACT_US_TITLE_2
        assert self.is_element_present(second_title), 'Second title is not presented'
        print('Second title is presented')
        assert 'GET IN TOUCH' in self.find(second_title).text, f'Second title should be: "GET IN TOUCH" got: {self.find(second_title).text}'
        print(f'Second title is correct: {self.find(second_title).text}')

    @allure.step("Заполнение имени")
    def fill_in_name_field(self):
        name_field = ContactUsPageLocators.NAME_FIELD
        name = DataGenerator.get_generated_data('first_name')
        assert self.is_element_present(name_field), 'Name field is not presented'
        print('Name field is presented')
        self.find(name_field).send_keys(name)
        print(f'Name field filled in with: {name}')

    @allure.step("Заполнение email")
    def fill_in_email_field(self):
        email_field = ContactUsPageLocators.EMAIL_FIELD
        email = DataGenerator.get_generated_data('email')
        assert self.is_element_present(email_field), 'Email field is not presented'
        print('Email field is presented')
        self.find(email_field).send_keys(email)
        print(f'Email field filled in with: {email}')

    @allure.step("Заполнение темы")
    def fill_in_subject_field(self):
        subject_field = ContactUsPageLocators.SUBJECT_FIELD
        subject = DataGenerator.get_subject()
        assert self.is_element_present(subject_field), 'Subject field is not presented'
        print('Subject field is presented')
        self.find(subject_field).send_keys(subject)
        print(f'Subject field filled in with: {subject}')

    @allure.step("Заполнение сообщения")
    def fill_in_message_field(self):
        message_field = ContactUsPageLocators.SUBJECT_FIELD
        message = DataGenerator.get_message()
        assert self.is_element_present(message_field), 'Message field is not presented'
        print(f'Message field is presented')
        self.find(message_field).send_keys(message)
        print(f'Message field filled in with: {message}')

    @allure.step("Нажатие кнопки отправки")
    def click_submit_button(self):
        submit_button = ContactUsPageLocators.SUBMIT_BUTTON
        assert self.is_element_present(submit_button), 'Submit button is not presented'
        print('Submit button is presented')
        self.find(submit_button).click()

    @allure.step("Переход на главную страницу")
    def go_to_home_page(self):
        home_button = (ContactUsPageLocators.HOME_BUTTON)
        assert self.is_element_present(home_button), 'Home button is not presented'
        print('Home button is presented')
        self.find(home_button).click()
        print('Home button is clicked')

    @allure.step("Проверка сообщения об успехе")
    def should_be_correct_success_message(self):
        success_message = ContactUsPageLocators.SUCCESS_MESSAGE
        success_message_text = self.find(success_message).text
        assert self.is_element_present(success_message), 'Success message is not presented'
        print('Success message is presented')
        assert 'Success! Your details have been submitted successfully.' in success_message_text, f'Success message should be: "Success! Your details have been submitted successfully." got:{success_message_text}'
        print('Success message is correct')

    @allure.step("Загрузка файла")
    def upload_contact_us_file(self):
        upload_field = ContactUsPageLocators.UPLOAD_FILE
        assert self.is_element_present(upload_field), 'Upload field is not presented'
        print('Upload field is presented')
        self.upload_file(upload_field)
        print('File uploaded')




