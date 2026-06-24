import json
import os
import random
from faker import Faker

class DataGenerator:
    @staticmethod
    def generate_data_for_registration(fields=None):
        fake = Faker('en_US')
        data = {
            'title': lambda: random.choice(['Mr.', 'Mrs.']),
            'first_name': fake.first_name,
            'last_name': fake.last_name,
            'email': fake.email,
            'password': lambda: fake.password(length=8, special_chars=True),
            'day_of_birth': lambda: str(random.randint(1, 28)),
            'month_of_birth': lambda: str(random.randint(1, 12)),
            'year_of_birth': lambda: str(random.randint(1900, 2023)),
            'newsletter': lambda: fake.boolean(chance_of_getting_true=50),
            'offers': lambda: fake.boolean(chance_of_getting_true=50),
            'company': fake.company,
            'address_1': fake.street_address,
            'address_2': fake.secondary_address,
            'city': fake.city,
            'state': fake.state,
            'country': lambda: random.choice(
                ['India', 'United States', 'Canada', 'Australia', 'Israel', 'New Zealand', 'Singapore']),
            'zipcode': fake.postcode,
            'mobile_number': fake.phone_number
        }

        if fields is None:
            data = {key: generator() for key, generator in data.items()}
            filename = 'registration_data.json'
        else:
            if isinstance(fields, str):
                fields = [fields]
            data = {field: data[field]() for field in fields if field in data}
            filename = 'generated_data.json'

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


    @staticmethod
    def get_registration_data(field):
        with open('registration_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)[field]
    
    @staticmethod
    def get_login_data(field):
        env_var = os.getenv(f'LOGIN_{field.upper()}')
        if env_var:
            return env_var
        with open('login_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)[field]

    @staticmethod
    def get_generated_data(fields):
        with open('generated_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)[fields]

    @staticmethod
    def get_subject():
        subject = Faker('en_US').text(10)
        return subject

    @staticmethod
    def get_message():
        message = Faker('en_US').text(100)
        return message

    @staticmethod
    def generate_card_info():
        fake = Faker('en_US')
        data = {
            'name_on_card': f'{DataGenerator.get_registration_data('first_name')} {DataGenerator.get_registration_data('last_name')}' or 'Bob Marley',
            'card_number': fake.credit_card_number(),
            'cvc': fake.credit_card_security_code(),
            'expiration_m': str(random.randint(1, 12)),
            'expiration_y': str(random.randint(2020, 2026))
        }
        filename = 'generated_card_data.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def get_card_info(field):
        with open('generated_card_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)[field]

