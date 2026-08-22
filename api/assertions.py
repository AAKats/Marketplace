import allure


@allure.step("Проверка статус-кода ответа")
def assert_status_code(response, expected_code):
    assert response.status_code == expected_code, \
        f'Expected status code {expected_code}, got {response.status_code}'
    print(f'Status code correct: {response.status_code}')


@allure.step("Проверка responseCode в теле ответа")
def assert_response_code(data, expected_code):
    assert 'responseCode' in data, 'responseCode is missing'
    assert data['responseCode'] == expected_code, \
        f'Expected responseCode {expected_code}, got {data["responseCode"]}'
    print(f'ResponseCode correct {data["responseCode"]}')


@allure.step("Проверка наличия ключа в ответе")
def assert_json_has_key(data, key):
    assert key in data, f'Key "{key}" is missing in response'
    print(f'Response contains key: "{key}"')


@allure.step("Проверка что список товаров не пустой")
def assert_products_not_empty(products):
    assert len(products) > 0, 'Products list is empty'
    print(f'Products list length correct: {len(products)}')


@allure.step("Проверка обязательных полей товара")
def assert_product_fields(product):
    required_fields = ['id', 'name', 'price', 'brand', 'category']
    for field in required_fields:
        assert field in product, f'Product with id = {product['id']} missing field "{field}"'
        print(f'Product with id = {product['id']} contains field: "{field}"')


@allure.step("Проверка структуры ответа списка товаров")
def assert_products_response(response, expected_code=200):
    assert_status_code(response, expected_code)
    data = response.json()
    assert_response_code(data, expected_code)
    assert_json_has_key(data, 'products')
    assert_products_not_empty(data['products'])
    for product in data['products']:
        assert_product_fields(product)

@allure.step("Проверка сообщения в ответе")
def assert_response_message(response, expected_message):
    message = response['message']
    assert expected_message in message, f'Incorrect response message: "{message}", should be: "{expected_message}"'
    print(f'Response message correct: "{message}"')

@allure.step("Проверка что список брендов не пустой")
def assert_brands_not_empty(brands):
    assert len(brands) > 0, 'Brands list is empty'
    print(f'Brands list length correct: {len(brands)}')

@allure.step("Проверка обязательных полей бренда")
def assert_brand_fields(brand):
    required_fields = ['id', 'brand']
    for field in required_fields:
        assert field in brand, f'Brand with id = {brand['id']} missing field "{field}"'
        print(f'Brand with id = {brand['id']} contains field: "{field}"')

@allure.step("Проверка структуры ответа списка брендов")
def assert_brands_response(response, expected_code=200):
    assert_status_code(response, expected_code)
    data = response.json()
    assert_response_code(data, expected_code)
    assert_json_has_key(data, 'brands')
    assert_brands_not_empty(data['brands'])
    for brand in data['brands']:
        assert_brand_fields(brand)

@allure.step("Проверка структуры ответа поиска товара")
def assert_searched_products(response, expected_code=200, search_term: str = ''):
    assert_response_code(response, expected_code)
    assert_json_has_key(response, 'products')
    assert_products_not_empty(response['products'])
    for product in response['products']:
        assert_product_fields(product)
        # Проверка что поисковый запрос есть в имени товара
        assert search_term in product['name'].lower(), \
            f'Product: "{product["name"]}" does not contain search term: "{search_term}"'
        print(f'Product name: "{product['name']}" contains search term: {search_term}')