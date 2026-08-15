import random
from encodings import search_function
from random import Random
from time import sleep
from turtledemo.sorting_animate import enable_keys

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utils.data_generator import DataGenerator
from ..locators import ProductsPageLocators, ProductPageLocators
from ..pages.base_page import BasePage


class ProductsPage(BasePage):
    '''Методы страницы продуктов'''

    def __init__(self, browser):
        super().__init__(browser)
        self.found_name = None
        self.selected_product = []

    @allure.step("Проверка списка товаров")
    def should_be_products_list(self):
        assert self.is_element_present(ProductsPageLocators.PRODUCTS_LIST), 'Products list is not presented'
        print('Products list is presented')

    @allure.step(f"Открытие товара")
    def click_view_product_by_number(self, number: int = None):
        products_list = self.find_elements(ProductsPageLocators.VIEW_PRODUCT_BUTTONS)
        if not number:
            number = random.randint(1, len(products_list) - 1)
        product = products_list[number]
        product_id = product.get_attribute('href').split('/product_details/')[-1]
        product.click()
        print(f'View button for the {number} product from the start (id = {product_id}) clicked')
        self.is_link_correct(f'product_details/{product_id}')

    @allure.step("Проверка полей товара")
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

    @allure.step("Поиск товара")
    def search_product(self, product_name = None):
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
        return product_name

    @allure.step("Проверка найденного товара")
    def check_found_product_name(self):
        product_names = self.find_elements(ProductsPageLocators.PRODUCT_NAMES)
        assert len(product_names) >= 1, 'Products not found'
        print(f'{len(product_names)} products found')
        for name in product_names:
            product_name = name.text
            assert self.found_name in product_name, f'{self.found_name} is not in {product_name}'
            print(f'"{product_name}" product found, and contains "{self.found_name}"')

    @allure.step("Проверка заголовка товаров")
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

    @allure.step("Добавление товаров в корзину")
    def add_products_to_cart(self, short: bool = False, all : bool = False, quantity: int = 1, count : int = 1,
                             first_number : int = 0):
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
                    print(f'Product {self.selected_product[product_index]['name']} added, quantity '
                          f'{self.selected_product[product_index]['quantity']}')

        elif count >= 2:
            assert first_number + count * 2 <= len(buttons) - 1, (f'Указанное количество товаров для добавления в '
                                                                  f'корзину недоступно, максимальное количество '
                                                                  f'{len(buttons)//2}')
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
                    if index == first_number + (count - 1) * 2 and _ == quantity - 1 and not short:
                        self.go_to_cart_via_modal()
                    elif not short:
                        self.continue_shoping()
                    print(f'Product {self.selected_product[product_index]['name']} added, quantity '
                          f'{self.selected_product[product_index]['quantity']}')
        else:
            for index in range(first_number, first_number + 2, 2):
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
                    if index == first_number + (count - 1) * 2 and _ == quantity - 1 and not short:
                        self.go_to_cart_via_modal()
                    elif not short:
                        self.continue_shoping()
                    print(f'Product {self.selected_product[product_index]['name']} added, quantity '
                          f'{self.selected_product[product_index]['quantity']}')
        return self.selected_product

    @allure.step("Открытие случайной карточки товара")
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

    @allure.step("Выбор категории товара")
    def select_category(self, category_name: str = None):
        css = ProductsPageLocators.CATEGORY_BUTTON_CSS.format(category_name)
        locator = (By.CSS_SELECTOR, css)
        self.is_element_present(locator)
        category_button = self.find(locator)
        category_button.click()
        print(f'{category_button.text.capitalize()} category selected')
        return category_name

    @allure.step("Выбор подкатегории товара")
    def select_subcategory(self, category: str, subcategory_name: str):
        css = ProductsPageLocators.SUBCATEGORY_BUTTON_CSS.format(category)
        elements = self.find_elements((By.CSS_SELECTOR, css))
        self.is_element_visible(elements[1])
        for el in elements:
            if subcategory_name.strip().lower() in el.text.strip().lower():
                category_text = el.text.strip()
                el.click()
                print(f'{category_text} subcategory selected')
                return category_text
        raise AssertionError(f'Subcategory "{subcategory_name}" not found in {category}')

    @allure.step("Проверка заголовка выбранной категории и подкатегории")
    def should_be_correct_category_title(self, category, subcategory):
        self.is_element_present(ProductsPageLocators.FILTERED_CATEGORY_TITLE)
        title = self.find(ProductsPageLocators.FILTERED_CATEGORY_TITLE)
        assert category.upper() in title.text and subcategory.upper() in title.text, (f'Incorrect title text: '
                                                                                      f'"{title.text}" should be: '
                                                                                      f'"{category.upper()} - '
                                                                                      f'{subcategory.upper()} '
                                                                                      f'PRODUCTS"')
        print(f'Category title is correct: "{title.text}"')

    @allure.step("Выбор бренда товара")
    def select_brand(self, brand_name: str = None):
        css = ProductsPageLocators.BRANDS_BUTTON_CSS.format(brand_name)
        locator = (By.CSS_SELECTOR, css)
        self.is_element_present(locator)
        brand_button = self.find(locator)
        brand_text = brand_button.text
        brand_button.click()
        print(f'{brand_text.capitalize()} brand selected')
        return brand_name

    @allure.step("Проверка заголовка выбранного бренда")
    def should_be_correct_brand_title(self, brand):
        self.is_element_present(ProductsPageLocators.FILTERED_BRAND_TITLE)
        title = self.find(ProductsPageLocators.FILTERED_BRAND_TITLE)
        assert brand.upper() in title.text.upper(), (f'Incorrect title text: "{title.text}" should be: '
                                                     f'"BRAND - {brand.upper()} PRODUCTS"')
        print(f'Category title is correct: "{title.text}"')

    @allure.step("Прокрутка до рекомендованных товаров")
    def scroll_to_recommended_items(self):
        self.scroll_to_element(ProductsPageLocators.RECOMMENDED_SECTION)
        print('Scrolled to recommended items')

    @allure.step("Проверка заголовка рекомендуемых товаров")
    def should_be_correct_recommended_title(self):
        self.is_element_present(ProductsPageLocators.RECOMMENDED_ITEMS_TITLE)
        self.is_element_visible(ProductsPageLocators.RECOMMENDED_ITEMS_TITLE)
        title = self.find(ProductsPageLocators.RECOMMENDED_ITEMS_TITLE)
        assert 'RECOMMENDED ITEMS' in title.text.upper(), (f'Incorrect title text: "{title.text}" should be: '
                                                     'RECOMMENDED ITEMS')
        print(f'Recommended items title is correct: "{title.text}"')

    @allure.step("Переключение слайда карусели рекомендованных товаров")
    def click_next_recommended_slide(self):
        next_btn = self.browser.find_element(
            By.CSS_SELECTOR, '.recommended-item-control.right'
        )
        next_btn.click()
        import time;
        time.sleep(0.5)
        print('Switched to next recommended items slide')

    def _extract_product_info(self, card):
        name = card.find_element(*ProductsPageLocators.RECOMMENDED_PRODUCT_NAME).get_attribute('textContent')
        price_text = card.find_element(*ProductsPageLocators.RECOMMENDED_PRODUCT_PRICE).get_attribute('textContent')
        price = price_text.replace('Rs. ', '')
        add_btn = card.find_element(*ProductsPageLocators.RECOMMENDED_ADD_TO_CART)
        product_id = add_btn.get_attribute('data-product-id')
        return {'id': product_id, 'name': name, 'price': price}

    @allure.step("Получение информации о рекомендованных товарах")
    def get_recommended_products_info(self):
        products = []
        seen_ids = set()

        # Собираем товары с видимого слайда
        cards = self.find_elements(ProductsPageLocators.RECOMMENDED_PRODUCT_CARDS)
        for card in cards:
            product = self._extract_product_info(card)
            if product['id'] not in seen_ids:
                seen_ids.add(product['id'])
                products.append(product)

        # Переключаем слайды и собираем оставшиеся
        for _ in range(5):
            prev_count = len(products)
            self.click_next_recommended_slide()
            cards = self.find_elements(ProductsPageLocators.RECOMMENDED_PRODUCT_CARDS)
            for card in cards:
                product = self._extract_product_info(card)
                if product['id'] not in seen_ids:
                    seen_ids.add(product['id'])
                    products.append(product)
            # Если новые товары не появились — все слайды пройдены
            if len(products) == prev_count:
                break

        print(f'Found {len(products)} recommended products')
        return products

    @allure.step("Добавление рекомендованного товара в корзину (id={product_id})")
    def add_recommended_product_to_cart(self, product_id, products, quantity=1):
        product = [p for p in products if p['id'] == str(product_id)][0]
        for _ in range(quantity):
            add_button = self.browser.find_element(
                By.CSS_SELECTOR,
                f'.recommended_items a[data-product-id="{product_id}"]'
            )
            add_button.click()
            if _ < quantity - 1:
                self.continue_shoping()
            print(f'Recommended product "{product["name"]}" added to cart, quantity {_ + 1}')
        product['quantity'] = quantity
        return product
