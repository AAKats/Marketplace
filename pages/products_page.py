import random
from encodings import search_function
from random import Random

from selenium.webdriver import ActionChains

from ..locators import ProductsPageLocators, ProductPageLocators
from ..pages.base_page import BasePage


class ProductsPage(BasePage):
    '''Методы страницы продуктов'''

    def __init__(self, browser):
        super().__init__(browser)
        self.found_name = None
        self.selected_product = []

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

    def continue_shoping(self):
        continue_button = ProductsPageLocators.CONTINUE_SHOPPING_BUTTON
        self.is_element_clickable(continue_button)
        self.find(continue_button).click()


    def add_products_to_cart(self, all : bool = False, quantity: int = 1, count : int = 1, first_number : int = 0):
        buttons = self.find_elements(ProductsPageLocators.ADD_TO_CART_BUTTONS)
        product_names = self.find_elements(ProductsPageLocators.PRODUCT_NAMES)
        product_prices = self.find_elements(ProductsPageLocators.PRODUCT_PRICES)

        if all:
            for index in range(0, len(buttons) - 1, 2):
                overlay_index = index + 1
                product_index = index // 2
                self.selected_product.append({
                    'name': product_names[product_index].text,
                    'price': product_prices[product_index].text[4:],
                    'quantity': 0
                })
                for _ in range(quantity):
                    ActionChains(self.browser).move_to_element(buttons[index]).perform()
                    self.is_element_visible(buttons[overlay_index])
                    buttons[overlay_index].click()
                    self.selected_product[-1]['quantity'] += 1
                    if index == len(buttons) - 2 and _ == quantity - 1:
                        self.go_to_cart_via_modal()
                    else:
                        self.continue_shoping()
                    print(f'Product {self.selected_product[product_index]['name']} added, quantity {self.selected_product[product_index]['quantity']}')

        elif count >= 2:
            assert first_number + count * 2 <= len(buttons) - 1, f'Указанное количество товаров для добавления в корзину недоступно, максимальное количество {len(buttons)//2}'
            for index in range(first_number, first_number + count * 2, 2):
                overlay_index = index + 1
                product_index = index // 2
                self.selected_product.append({
                    'name': product_names[product_index].text,
                    'price': product_prices[product_index].text[4:],
                    'quantity': 0
                })
                for _ in range(quantity):
                    ActionChains(self.browser).move_to_element(buttons[index]).perform()
                    self.is_element_visible(buttons[overlay_index])
                    buttons[overlay_index].click()
                    self.selected_product[-1]['quantity'] += 1
                    if index == first_number + (count - 1) * 2 and _ == quantity - 1:
                        self.go_to_cart_via_modal()
                    else:
                        self.continue_shoping()
                    print(f'Product {self.selected_product[product_index]['name']} added, quantity {self.selected_product[product_index]['quantity']}')
        return self.selected_product

    def open_random_product(self):
        products = self.find_elements(ProductsPageLocators.VIEW_PRODUCT_BUTTON)
        product_prices = self.find_elements(ProductsPageLocators.PRODUCT_PRICES)
        product_names = self.find_elements(ProductsPageLocators.PRODUCT_NAMES)
        index = random.randrange(0, len(products) - 1)
        product = products[index]
        product_id = product.get_attribute('href').split('/product_details/')[-1]

        self.selected_product = {
            'name': product_names[index].text,
            'price': product_prices[index].text[4:],
            'id': product_id
        }
        product.click()
        print(f'Product "{self.selected_product["name"]}" (ID: {product_id}) opened')
        return self.selected_product




