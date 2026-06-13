from tabnanny import check

import pytest

from ..pages.products_page import ProductsPage


class TestProductsPage:

    @pytest.mark.view_product
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_products_page(self,browser):
        page = ProductsPage(browser)
        page.open()
        page.go_to_products_page()
        page.is_link_correct('products')
        page.should_be_products_list()
        page.click_view_product_by_number(1)
        page.should_be_product_info_fields()

    @pytest.mark.search_product
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_search_product(self,browser):
        page = ProductsPage(browser)
        page.open()
        page.go_to_products_page()
        page.search_random_product('Sleeveless')
        page.check_found_product_name()
        page.should_be_correct_title()


