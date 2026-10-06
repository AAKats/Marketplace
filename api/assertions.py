import allure

from utils.data_generator import DataGenerator


@allure.step("Проверка статус-кода ответа")
def assert_status_code(response, expected_code):
    """Проверка HTTP статус-кода ответа"""
    assert response.status_code == expected_code, \
        f'Expected status code {expected_code}, got {response.status_code}'
    print(f'Status code correct: {response.status_code}')


@allure.step("Проверка responseCode в теле ответа")
def assert_response_code(data, expected_code):
    """Проверка responseCode в JSON теле ответа"""
    assert 'responseCode' in data, 'responseCode is missing'
    assert data['responseCode'] == expected_code, \
        f'Expected responseCode {expected_code}, got {data["responseCode"]}'
    print(f'ResponseCode correct: {data["responseCode"]}')


@allure.step("Проверка наличия ключа в ответе")
def assert_json_has_key(data, key):
    """Проверка наличия ключа в JSON объекте"""
    assert key in data, f'Key "{key}" is missing in response'
    print(f'Response contains key: "{key}"')


@allure.step("Проверка что список товаров не пустой")
def assert_products_not_empty(products):
    """Проверка что список товаров не пустой"""
    assert len(products) > 0, 'Products list is empty'
    print(f'Products list length correct: {len(products)}')


@allure.step("Проверка обязательных полей товара")
def assert_product_fields(product):
    """Проверка наличия обязательных полей в объекте товара"""
    required_fields = ['id', 'name', 'price', 'brand', 'category']
    for field in required_fields:
        assert field in product, f'Product with id = {product['id']} missing field "{field}"'
        print(f'Product with id = {product['id']} contains field: "{field}"')


@allure.step("Проверка структуры ответа списка товаров")
def assert_products_response(response, expected_code=200):
    """Проверка полной структуры ответа списка товаров"""
    assert_status_code(response, expected_code)
    data = response.json()
    assert_response_code(data, expected_code)
    assert_json_has_key(data, 'products')
    assert_products_not_empty(data['products'])
    for product in data['products']:
        assert_product_fields(product)

@allure.step("Проверка сообщения в ответе")
def assert_response_message(response, expected_message):
    """Проверка сообщения в JSON теле ответа"""
    message = response['message']
    assert expected_message in message, f'Incorrect response message: "{message}", should be: "{expected_message}"'
    print(f'Response message correct: "{message}"')

@allure.step("Проверка что список брендов не пустой")
def assert_brands_not_empty(brands):
    """Проверка что список брендов не пустой"""
    assert len(brands) > 0, 'Brands list is empty'
    print(f'Brands list length correct: {len(brands)}')

@allure.step("Проверка обязательных полей бренда")
def assert_brand_fields(brand):
    """Проверка наличия обязательных полей в объекте бренда"""
    required_fields = ['id', 'brand']
    for field in required_fields:
        assert field in brand, f'Brand with id = {brand['id']} missing field "{field}"'
        print(f'Brand with id = {brand['id']} contains field: "{field}"')

@allure.step("Проверка структуры ответа списка брендов")
def assert_brands_response(response, expected_code=200):
    """Проверка полной структуры ответа списка брендов"""
    assert_status_code(response, expected_code)
    data = response.json()
    assert_response_code(data, expected_code)
    assert_json_has_key(data, 'brands')
    assert_brands_not_empty(data['brands'])
    for brand in data['brands']:
        assert_brand_fields(brand)

@allure.step("Проверка структуры ответа поиска товара")
def assert_searched_products(response, expected_code=200, search_term: str = ''):
    """Проверка структуры ответа поиска товаров и наличие поискового запроса в имени"""
    assert_response_code(response, expected_code)
    assert_json_has_key(response, 'products')
    assert_products_not_empty(response['products'])
    for product in response['products']:
        assert_product_fields(product)
        # Проверка что поисковый запрос есть в имени товара
        assert search_term in product['name'].lower(), \
            f'Product: "{product['name']}" does not contain search term: "{search_term}"'
        print(f'Product name: "{product['name']}" contains search term: {search_term}')

@allure.step("Проверка что данные о пользователе не пустые")
def assert_user_details_not_empty(user):
    """Проверка что данные о пользователе не пустые"""
    assert isinstance(user, dict) and len(user) > 0, 'User details are empty'
    print(f'User details not empty: {len(user)} fields')

@allure.step("Проверка обязательных полей данных о пользователе")
def assert_user_details_fields(user):
    """Проверка наличия обязательных полей в данных пользователя"""
    required_fields = ['id', 'name', 'email', 'title', 'birth_day', 'birth_month', 'birth_year', 'first_name',
                       'last_name', 'company', 'address1', 'address2', 'country', 'state', 'city', 'zipcode']
    for field in required_fields:
        assert field in user, f'User detail with id = {user['id']} missing field "{field}"'
        print(f'User detail with name = {user['id']} contains field: "{field}"')

@allure.step("Проверка структуры ответа данных пользователя")
def assert_user_details_response(response, expected_code=200):
    """Проверка полной структуры ответа данных пользователя"""
    assert_status_code(response, expected_code)
    data = response.json()
    assert_response_code(data, expected_code)
    assert_json_has_key(data, 'user')
    assert_user_details_not_empty(data['user'])
    assert_user_details_fields(data['user'])

@allure.step("Проверка данных по пользователю")
def assert_user_data(response, expected_code=200):
    """Проверка данных пользователя в ответе API с данными из DataGenerator"""
    assert_response_code(response, expected_code)
    user = response['user']
    reg_data = DataGenerator.get_registration_data()

    fields = {
        'email': reg_data['email'],
        'title': reg_data['title'],
        'birth_day': reg_data['day_of_birth'],
        'birth_month': reg_data['month_of_birth'],
        'birth_year': reg_data['year_of_birth'],
        'first_name': reg_data['first_name'],
        'last_name': reg_data['last_name'],
        'company': reg_data['company'],
        'address1': reg_data['address_1'],
        'address2': reg_data['address_2'],
        'country': reg_data['country'],
        'state': reg_data['state'],
        'city': reg_data['city'],
        'zipcode': reg_data['zipcode'],
    }

    for field, expected in fields.items():
        assert field in user, f'Field "{field}" missing in payload'
        assert user[field] == expected, \
            f'Field "{field}": expected "{expected}", got "{user[field]}"'
        print(f'Payload field "{field}" correct: "{user[field]}"')

