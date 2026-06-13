from ..client import ApiClient
from ...utils.data_generator import DataGenerator

class UserApi(ApiClient):
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
        response = self.post("/api/createAccount", data=payload) 
        return response
