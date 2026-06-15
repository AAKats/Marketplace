import random

from locators import ProductPageLocators
from ..utils.data_generator import DataGenerator

from ..locators import BasePageLocators
from ..pages.base_page import BasePage


class ProductPage(BasePage):
    '''Методы для страницы карточки товара'''

    def select_quantity_of_product(self):
        self.is_element_present(ProductPageLocators.QUANTITY_FIELD)
        quantity_field = self.find(ProductPageLocators.QUANTITY_FIELD)
        quantity = random.randrange(1,10)
        quantity_field.clear()
        quantity_field.send_keys(quantity)
        print(f'Quantity = {quantity} selected')
        return quantity

    def add_product_to_cart(self):
        self.is_element_present(ProductPageLocators.ADD_TO_CART_BUTTON)
        self.find(ProductPageLocators.ADD_TO_CART_BUTTON).click()
        print('Product was added to cart')

