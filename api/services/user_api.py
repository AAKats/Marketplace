import allure

from ..client import ApiClient
from utils.data_generator import DataGenerator

class UserApi(ApiClient):
    @allure.step("Создание пользователя через API")
    def create_account(self, name = None, email = None, password = None, **kwargs):
        """Создание пользователя через API (обход UI регистрации)"""
        payload = {
            "name": name or DataGenerator.get_registration_data('first_name'), 
            "email": email or DataGenerator.get_registration_data('email'), 
            "password": password or DataGenerator.get_registration_data('password'), 
            "title": DataGenerator.get_registration_data('title'), 
            "birth_day": DataGenerator.get_registration_data('day_of_birth'), 
            "birth_month": DataGenerator.get_registration_data('month_of_birth'), 
            "birth_year": DataGenerator.get_registration_data('year_of_birth'), 
            "firstname": DataGenerator.get_registration_data('first_name'), 
            "lastname": DataGenerator.get_registration_data('last_name'), 
            "company": DataGenerator.get_registration_data('company'), 
            "address1": DataGenerator.get_registration_data('address_1'), 
            "country": DataGenerator.get_registration_data('country'), 
            "state": DataGenerator.get_registration_data('state'), 
            "city": DataGenerator.get_registration_data('city'), 
            "zipcode": DataGenerator.get_registration_data('zipcode'), 
            "mobile_number":  DataGenerator.get_registration_data('mobile_number'), 
        }
        payload.update(kwargs)
        print('New user details:')
        for key, value in payload.items():
            print(f'  {key}: {value}')
        response = self.post("/api/createAccount", data=payload) 
        return response

    @allure.step("POST запрос verifyLogin с валидными данными")
    def send_post_to_verify_login_with_valid_details(self, email = None, password = None):
        """POST запрос verifyLogin с валидными данными"""
        payload = {
            "email": email or DataGenerator.get_login_data('email'),
            "password": password or DataGenerator.get_login_data('password'),
        }
        response = self.post("/api/verifyLogin", data=payload)
        return response

    @allure.step("POST запрос verifyLogin без email")
    def send_post_to_verify_login_without_email(self, password = None):
        """POST запрос verifyLogin без email"""
        payload = {
            "password": password or DataGenerator.get_login_data('password'),
        }
        response = self.post("/api/verifyLogin", data=payload)
        return response

    @allure.step("DELETE запрос verifyLogin")
    def send_delete_to_verify_login(self):
        """DELETE запрос verifyLogin"""
        response = self.delete("/api/verifyLogin")
        return response

    @allure.step("Удаление пользователя через API")
    def delete_registered_user(self, email = None, password = None):
        """Удаление пользователя через API"""
        payload = {
            "email": email or DataGenerator.get_registration_data('email'),
            "password": password or DataGenerator.get_registration_data('password'),
        }
        response = self.delete("/api/deleteAccount", data=payload)
        return response

    @allure.step("Обновление данных пользователя через PUT")
    def update_account_via_put(self, name = None, email = None, password = None, **kwargs):
        """Обновление пользователя через API"""
        payload = {
            "name": name or DataGenerator.get_registration_data('first_name'),
            "email": email or DataGenerator.get_registration_data('email'),
            "password": password or DataGenerator.get_registration_data('password'),
            "title": DataGenerator.get_registration_data('title'),
            "birth_day": DataGenerator.get_registration_data('day_of_birth'),
            "birth_month": DataGenerator.get_registration_data('month_of_birth'),
            "birth_year": DataGenerator.get_registration_data('year_of_birth'),
            "firstname": DataGenerator.get_registration_data('first_name'),
            "lastname": DataGenerator.get_registration_data('last_name'),
            "company": DataGenerator.get_registration_data('company'),
            "address1": DataGenerator.get_registration_data('address_1'),
            "country": DataGenerator.get_registration_data('country'),
            "state": DataGenerator.get_registration_data('state'),
            "city": DataGenerator.get_registration_data('city'),
            "zipcode": DataGenerator.get_registration_data('zipcode'),
            "mobile_number": DataGenerator.get_registration_data('mobile_number'),
        }
        payload.update(kwargs)
        print('Updated user details:')
        for key, value in payload.items():
            print(f'  {key}: {value}')
        response = self.put("/api/updateAccount", data=payload)
        return response

    @allure.step("Получение данных пользователя по email")
    def get_account_details(self, email=None):
        """Получение данных пользователя по email"""
        payload = {
            "email": email or DataGenerator.get_registration_data('email')
        }
        response = self.get("/api/getUserDetailByEmail", params=payload)
        return response