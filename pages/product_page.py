import random

import allure

from locators import ProductPageLocators
from ..utils.data_generator import DataGenerator
from ..pages.base_page import BasePage


class ProductPage(BasePage):
    '''Методы для страницы карточки товара'''

    @allure.step("Выбор количество единиц товара")
    def select_quantity_of_product(self):
        self.is_element_present(ProductPageLocators.QUANTITY_FIELD)
        quantity_field = self.find(ProductPageLocators.QUANTITY_FIELD)
        quantity = random.randrange(1,10)
        quantity_field.clear()
        quantity_field.send_keys(quantity)
        print(f'Quantity = {quantity} selected')
        return quantity

    @allure.step("Добавление товара в корзину")
    def add_product_to_cart(self):
        self.is_element_present(ProductPageLocators.ADD_TO_CART_BUTTON)
        self.find(ProductPageLocators.ADD_TO_CART_BUTTON).click()
        print('Product was added to cart')

    @allure.step("Заполнение имени для отзыва о товаре")
    def fill_in_review_name_field(self):
        first_name, last_name =  DataGenerator.get_login_data('first_name','last_name')
        name = f'{first_name} {last_name}'
        self.is_element_present(ProductPageLocators.REVIEW_NAME_FIELD)
        name_field = self.find(ProductPageLocators.REVIEW_NAME_FIELD)
        name_field.send_keys(name)
        print(f'Review name field filled in with "{name}"')

    @allure.step("Заполнение почты для отзыва о товаре")
    def fill_in_review_email_field(self):
        email =  DataGenerator.get_login_data('email')
        self.is_element_present(ProductPageLocators.REVIEW_EMAIL_FIELD)
        email_field = self.find(ProductPageLocators.REVIEW_EMAIL_FIELD)
        email_field.send_keys(email)
        print(f'Review email field filled in with "{email}"')

    @allure.step("Заполнение отзыва о товаре")
    def fill_in_review_message_field(self):
        message = DataGenerator.get_message()
        self.is_element_present(ProductPageLocators.REVIEW_MESSAGE_FIELD)
        message_field = self.find(ProductPageLocators.REVIEW_MESSAGE_FIELD)
        message_field.send_keys(message)
        print(f'Review message field filled in with "{message}"')

    @allure.step("Отправка отзыва о товаре")
    def click_submit_review_button(self):
        self.is_element_present(ProductPageLocators.SUBMIT_REVIEW_BUTTON)
        submit_button = self.find(ProductPageLocators.SUBMIT_REVIEW_BUTTON)
        submit_button.click()
        print(f'Submit review button clicked')

    @allure.step("Проверка сообщения об успешном отзыве")
    def should_be_correct_success_review_message(self):
        success_message = self.is_element_visible(ProductPageLocators.SUCCESS_REVIEW_MESSAGE)
        assert 'Thank you for your review.' in success_message.text, \
            f'Incorrect success message: {success_message.text}'
        print(f'Success review message is displayed')

