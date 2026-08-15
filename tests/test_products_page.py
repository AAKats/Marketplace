import allure
import pytest

from ..pages.products_page import ProductsPage


class TestProductsPage:

    @allure.feature('Products')
    @allure.story('Просмотр карточки товара')
    @allure.severity(allure.severity_level.CRITICAL)
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

    @allure.feature('Products')
    @allure.story('Поиск товара')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.search_product
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_search_product(self,browser):
        page = ProductsPage(browser)
        page.open()
        page.go_to_products_page()
        page.search_product('Sleeveless')
        page.should_be_correct_title()
        page.check_found_product_name()

    @allure.feature('Products')
    @allure.story('Фильтрация товаров')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.filter_product
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.ui
    @pytest.mark.filter_product_by_category
    def test_filter_product_by_category(self, browser):
        page = ProductsPage(browser)
        page.open()
        page.go_to_products_page()
        category = page.select_category('Women')
        subcategory = page.select_subcategory(category, 'Dress')
        page.should_be_correct_category_title(category, subcategory)
        category = page.select_category('Men')
        subcategory = page.select_subcategory(category, 'Jeans')
        page.should_be_correct_category_title(category, subcategory)

    @allure.feature('Products')
    @allure.story('Фильтрация товаров')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.filter_product
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.ui
    @pytest.mark.filter_product_by_brand
    def test_filter_product_by_brand(self, browser):
        page = ProductsPage(browser)
        page.open()
        page.go_to_products_page()
        brand = page.select_brand('Polo')
        page.should_be_correct_brand_title(brand)
        brand = page.select_brand('H&M')
        page.should_be_correct_brand_title(brand)



