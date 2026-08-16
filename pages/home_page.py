import allure
from ..utils.data_generator import DataGenerator

from ..locators import BasePageLocators
from ..pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, *args, **kwargs):
        super(HomePage, self).__init__(*args, **kwargs)

    @allure.step("Проверка кнопки Contact Us")
    def should_be_contact_us_button(self):
        assert self.is_element_present(BasePageLocators.CONTACT_US_BUTTON), 'Contact us button is not presented'
        print('Contact us button is presented')




