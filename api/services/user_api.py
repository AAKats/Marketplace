from api.client import ApiClient

class UserApi(ApiClient):
    def create_account(self, name, email, password, **kwargs):
        """Создание пользователя через API (обход UI регистрации)"""
        payload = {
            "name": name, 
            "email": email, 
            "password": password,
            "title": "Mr",
            "birth_date": "01",
            "birth_month": "11",
            "birth_year": "2012",
            "firstname": name,
            "lastname": "Tester",
            "company": "TestCompany",
            "address1": "Kudykina gora 1",
            "country": "Russia",
            "state": "Moskovskaya oblast'",
            "city": "Kudykinsk",
            "zipcode": "192101",
            "mobile_number": "1234567890"
        }
        payload.update(kwargs)
        response = self.post("/api/createAccount", data=payload) 
        return response
