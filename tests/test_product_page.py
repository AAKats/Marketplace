import allure
import pytest

from ..pages.products_page import ProductsPage
from ..pages.product_page import ProductPage

class TestProductPage:

    @allure.feature('Products')
    @allure.story('Отправка отзыва на товар')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.view_product
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_review_product(self,browser):
        page = ProductsPage(browser)
        page.open()
        page.is_link_correct()
        page.click_view_product_by_number(11)
        page = ProductPage(browser)
        page.fill_in_review_name_field()
        page.fill_in_review_email_field()
        page.fill_in_review_message_field()
        page.click_submit_review_button()
        page.should_be_correct_success_review_message()
