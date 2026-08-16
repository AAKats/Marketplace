import allure
import pytest

from ..pages.cart_page import CartPage
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

    @allure.feature('Products')
    @allure.story('Добавление рекомендованных товаров в корзину')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.add_recommended_product
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_add_recommended_products_to_cart(self, browser):
        page = ProductsPage(browser)
        page.open()
        page.is_link_correct()
        page.scroll_to_recommended_items()
        page.should_be_correct_recommended_title()
        products = page.get_recommended_products_info()
        added_products = page.add_recommended_product_to_cart(1, products)
        page.go_to_cart_via_modal()
        cart = CartPage(browser, added_products)
        cart.cart_should_contain_correct_count_of_products(1)
        cart.check_product_name()
        cart.check_product_price()
        cart.check_product_quantity()

    @allure.feature('Products')
    @allure.story('Прокрутка страницы')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.scrolling
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.ui
    @pytest.mark.scrolling_with_angle_up
    def test_scrolling_with_angle_up(self, browser):
        page = ProductsPage(browser)
        page.open()
        page.is_link_correct()
        page.scroll_to_the_bottom()
        page.scroll_to_the_top_by_angle()

    @allure.feature('Products')
    @allure.story('Прокрутка страницы')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.scrolling
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.ui
    @pytest.mark.scrolling_down_and_back
    def test_scrolling(self, browser):
        page = ProductsPage(browser)
        page.open()
        page.is_link_correct()
        page.scroll_to_the_bottom()
        page.scroll_to_the_top()
