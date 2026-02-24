import json
import random
from faker import Faker

class DataGenerator:

    fake = Faker('en_US')

    def generate_data_for_registration(self):
        data = {
            'title': random.choice(['Mr.', 'Mrs.']),
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'email': self.fake.email(),
            'password': self.fake.password(length=8, special_chars=True),
            'day_of_birth': str(random.randint(1, 28)),
            'month_of_birth': str(random.randint(1, 12)),
            'year_of_birth': str(random.randint(1900, 2023)),
            'newsletter': self.fake.boolean(chance_of_getting_true=50),
            'offers': self.fake.boolean(chance_of_getting_true=50),
            'company': self.fake.company(),
            'address_1': self.fake.street_address(),
            'address_2': self.fake.secondary_address(),
            'city': self.fake.city(),
            'state': self.fake.state(),
            'country': random.choice(['India', 'United States','Canada','Australia','Israel','New Zealand','Singapore']),
            'zipcode': self.fake.postcode(),
            'mobile_number': self.fake.phone_number()
        }
        
        json_data = json.dumps(data, indent=4)
        print(json_data)
        with open('registration_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


    def get_registration_data(field):
        with open('registration_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)[field]