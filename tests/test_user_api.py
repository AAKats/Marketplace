import allure
import pytest

from api.assertions import assert_user_data, assert_user_details_response
from utils.data_generator import DataGenerator
from ..api.assertions import assert_status_code, assert_response_code, assert_response_message

class TestUserAPI:

    @allure.feature('User API')
    @allure.story('Проверка существования пользователя с корректными данными')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.api
    @pytest.mark.user_api
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.verify_login_with_valid_details
    def test_verify_login_with_valid_details(self, api_client):
        response = api_client.send_post_to_verify_login_with_valid_details()

        assert_status_code(response, 200)
        data = response.json()
        assert_response_code(data, 200)
        assert_response_message(data, 'User exists!')

    @allure.feature('User API')
    @allure.story('Проверка существования пользователя с пустым email')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.api
    @pytest.mark.user_api
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.verify_login_without_email
    def test_verify_login_without_email(self, api_client):
        response = api_client.send_post_to_verify_login_without_email()

        assert_status_code(response, 200)
        data = response.json()
        assert_response_code(data, 400)
        assert_response_message(data, 'Bad request, email or password parameter is missing in POST request.')

    @allure.feature('User API')
    @allure.story('Проверка существования пользователя методом delete')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.api
    @pytest.mark.user_api
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.verify_login_via_delete
    def test_verify_login_via_delete(self, api_client):
        response = api_client.send_delete_to_verify_login()

        assert_status_code(response, 200)
        data = response.json()
        assert_response_code(data, 405)
        assert_response_message(data, 'This request method is not supported.')

    @allure.feature('User API')
    @allure.story('Проверка существования пользователя с некорректными данными')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    @pytest.mark.user_api
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.verify_login_with_invalid_details
    def test_verify_login_with_invalid_details(self, api_client):
        response = api_client.send_post_to_verify_login_with_valid_details(email='invalid@email.com',
                                                                           password='invalid_password')

        assert_status_code(response, 200)
        data = response.json()
        assert_response_code(data, 404)
        assert_response_message(data, 'User not found!')

    @allure.feature('User API')
    @allure.story('Создание нового пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    @pytest.mark.user_api
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.create_user_account
    def test_create_user_account(self, api_client):
        DataGenerator.generate_data_for_registration()
        response = api_client.create_account()

        assert_status_code(response, 200)
        data = response.json()
        assert_response_code(data, 201)
        assert_response_message(data, 'User created!')

    @allure.feature('User API')
    @allure.story('Удаление существующего пользователя')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    @pytest.mark.user_api
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.delete_user_account
    def test_delete_user_account(self, api_client):
        DataGenerator.generate_data_for_registration()
        response= api_client.create_account()

        assert_status_code(response, 200)
        data = response.json()
        assert_response_code(data, 201)
        assert_response_message(data, 'User created!')

        response = api_client.delete_registered_user()

        assert_status_code(response, 200)
        data = response.json()
        assert_response_code(data, 200)
        assert_response_message(data, 'Account deleted!')

    @allure.feature('User API')
    @allure.story('Обновление данных для существующего пользователя')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    @pytest.mark.user_api
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.update_user_account
    def test_update_user_account(self, api_client):
        DataGenerator.generate_data_for_registration()
        response = api_client.create_account()

        assert_status_code(response, 200)
        data = response.json()
        assert_response_code(data, 201)
        assert_response_message(data, 'User created!')

        response = api_client.update_account_via_put()

        assert_status_code(response, 200)
        data = response.json()
        assert_response_code(data, 200)
        assert_response_message(data, 'User updated!')

    @allure.feature('User API')
    @allure.story('Получние данных существующего пользователя через email')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    @pytest.mark.user_api
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.get_user_details
    @pytest.mark.xfail(reason='BUG: Birth_ fields are empty in response')
    def test_get_user_details(self, api_client):
        DataGenerator.generate_data_for_registration()
        response = api_client.create_account()

        assert_status_code(response, 200)
        data = response.json()
        assert_response_code(data, 201)
        assert_response_message(data, 'User created!')

        get_response = api_client.get_account_details()

        assert_user_details_response(get_response)
        assert_status_code(get_response, 200)
        get_data = get_response.json()
        assert_response_code(get_data, 200)
        assert_user_data(get_data)


