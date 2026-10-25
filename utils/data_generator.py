import os
import random
import uuid

from faker import Faker


class DataGenerator:
    """Генератор тестовых данных.

    Все данные хранятся в памяти процесса: файлы в корне репозитория
    ломают параллельный запуск (pytest-xdist: воркеры перезаписывают
    файлы друг друга) и засоряют рабочую директорию.
    """

    _registration_data = None
    _generated_data = {}
    _card_info = None
    _existing_user = None

    @staticmethod
    def generate_data_for_registration(fields=None):
        """Генерирует полный профиль или отдельные поля.

        Полный профиль (fields=None) нужен фикстуре existing_user:
        все поля согласованы между собой. Отдельные поля — для форм,
        где регистрация не выполняется (подписка, contact us).
        """
        fake = Faker('en_US')
        generators = {
            'title': lambda: random.choice(['Mr.', 'Mrs.']),
            'first_name': fake.first_name,
            'last_name': fake.last_name,
            'email': lambda: f"{uuid.uuid4().hex[:8]}_{fake.email()}",
            'password': lambda: fake.password(length=8, special_chars=True),
            'day_of_birth': lambda: str(random.randint(1, 28)),
            'month_of_birth': lambda: str(random.randint(1, 12)),
            'year_of_birth': lambda: str(random.randint(1900, 2021)),
            'newsletter': lambda: fake.boolean(chance_of_getting_true=50),
            'offers': lambda: fake.boolean(chance_of_getting_true=50),
            'company': fake.company,
            'address_1': fake.street_address,
            'address_2': fake.secondary_address,
            'city': fake.city,
            'state': fake.state,
            'country': lambda: random.choice(
                ['India', 'United States', 'Canada', 'Australia',
                 'Israel', 'New Zealand', 'Singapore']),
            'zipcode': fake.postcode,
            'mobile_number': fake.phone_number,
        }

        if fields is None:
            DataGenerator._registration_data = {
                key: gen() for key, gen in generators.items()
            }
            return DataGenerator._registration_data

        if isinstance(fields, str):
            fields = [fields]
        data = {f: generators[f]() for f in fields if f in generators}
        DataGenerator._generated_data.update(data)
        return data

    @staticmethod
    def get_registration_data(*fields):
        if DataGenerator._registration_data is None:
            raise RuntimeError(
                'Профиль не сгенерирован: вызовите generate_data_for_registration() '
                '(обычно это делает фикстура existing_user в conftest)'
            )
        if not fields:
            return DataGenerator._registration_data

        env_values = [os.getenv(f'REGISTRATION_{f.upper()}') for f in fields]
        if all(env_values):
            return env_values[0] if len(fields) == 1 else tuple(env_values)

        values = [DataGenerator._registration_data[f] for f in fields]
        return values[0] if len(fields) == 1 else tuple(values)

    @staticmethod
    def set_existing_user(data: dict):
        """Сохраняет профиль пользователя, созданного через API."""
        DataGenerator._existing_user = dict(data)

    @staticmethod
    def get_login_data(*fields):
        if DataGenerator._existing_user is None:
            raise RuntimeError(
                'Нет данных для входа: задай env LOGIN_EMAIL/LOGIN_PASSWORD '
                'или используй фикстуру existing_user (регистрация через API)'
            )
        if not fields:
            return DataGenerator._existing_user

        env_values = [os.getenv(f'LOGIN_{f.upper()}') for f in fields]
        if all(env_values):
            return env_values[0] if len(fields) == 1 else tuple(env_values)

        values = [DataGenerator._existing_user[f] for f in fields]
        return values[0] if len(fields) == 1 else tuple(values)

    @staticmethod
    def get_generated_data(field):
        if field not in DataGenerator._generated_data:
            raise KeyError(
                f'Поле "{field}" не генерировалось: сначала вызовите '
                f'generate_data_for_registration(["{field}"])'
            )
        return DataGenerator._generated_data[field]

    @staticmethod
    def get_subject():
        return Faker('en_US').text(10)

    @staticmethod
    def get_message():
        return Faker('en_US').text(100)

    @staticmethod
    def generate_card_info():
        fake = Faker('en_US')
        DataGenerator._card_info = {
            'name_on_card': (
                f'{DataGenerator.get_registration_data("first_name")} '
                f'{DataGenerator.get_registration_data("last_name")}'
            ) or 'Bob Marley',
            'card_number': fake.credit_card_number(),
            'cvc': fake.credit_card_security_code(),
            'expiration_m': str(random.randint(1, 12)),
            'expiration_y': str(random.randint(2020, 2026)),
        }
        return DataGenerator._card_info

    @staticmethod
    def get_card_info(field):
        if DataGenerator._card_info is None:
            raise KeyError('Карта не генерировалась: сначала вызовите generate_card_info()')
        return DataGenerator._card_info[field]
