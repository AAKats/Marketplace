import random
from encodings import search_function

from ..locators import ProductsPageLocators, ProductPageLocators
from ..pages.base_page import BasePage


class ProductsPage(BasePage):
    '''Методы страницы продуктов'''

    def __init__(self, browser):
        super().__init__(browser)
        self.found_name = None

    def should_be_products_list(self):
        assert self.is_element_present(ProductsPageLocators.PRODUCTS_LIST), 'Products list is not presented'
        print('Products list is presented')

    def click_view_product_by_number(self, number):
        products_list = self.find_elements(ProductsPageLocators.VIEW_PRODUCT_BUTTONS)
        products_list[number - 1].click()
        print(f'View button for {number} is clicked')
        self.is_link_correct(f'product_details/{number}')

    def should_be_product_info_fields(self):
        assert self.is_element_present(ProductPageLocators.PRODUCT_NAME), 'Product name field is not presented'
        print('Product name field is presented')
        assert self.is_element_present(ProductPageLocators.CATEGORY), 'Category field is not presented'
        print('Category field is presented')
        assert self.is_element_present(ProductPageLocators.PRICE), 'Price field is not presented'
        print('Price field is presented')
        assert self.is_element_present(ProductPageLocators.AVAILABILITY), 'Availability field is not presented'
        print('Availability field is presented')
        assert self.is_element_present(ProductPageLocators.CONDITION), 'Condition field is not presented'
        print('Condition field is presented')
        assert self.is_element_present(ProductPageLocators.BRAND), 'Brand field is not presented'
        print('Brand field is presented')

    def search_random_product(self,product_name = None):
        if product_name is None:
            product_names = self.find_elements(ProductsPageLocators.PRODUCT_NAMES)
            product_name = random.choice(product_names).text
        self.found_name = product_name
        search_field = ProductsPageLocators.SEARCH_FIELD
        search_button = ProductsPageLocators.SEARCH_BUTTON
        assert self.is_element_present(search_field), 'Search field is not presented'
        print('Search field is presented')
        self.find(search_field).send_keys(product_name)
        print(f'Search field is filled in with: "{product_name}"')
        assert self.is_element_present(search_button), 'Search button is not presented'
        print('Search button is presented')
        self.find(search_button).click()
        print('Search button is clicked')

    def check_found_product_name(self):
        product_names = self.find_elements(ProductsPageLocators.PRODUCT_NAMES)
        assert len(product_names) >= 1, 'Products not found'
        print(f'{len(product_names)} products found')
        for name in product_names:
            product_name = name.text
            assert self.found_name in product_name, f'{self.found_name} is not in {product_name}'
            print(f'"{product_name}" product found, and contains "{self.found_name}"')

    def should_be_correct_title(self):
        title = ProductsPageLocators.TITLE
        title_text = self.find(title).text
        assert self.is_element_present(title), 'Title is not presented'
        print('Title is presented')
        assert 'SEARCHED PRODUCTS' in title_text, f'Title should be "SEARCHED PRODUCTS" got: {title_text}'
        print(f'Title {title_text} correct')






