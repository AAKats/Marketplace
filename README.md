# Marketplace Test Automation

Проект автоматизации тестирования веб-приложения с использованием Selenium и pytest.

## Технологии

- **Python** — язык программирования
- **pytest** — тестовый фреймворк
- **Selenium WebDriver** — для UI-тестирования
- **requests** — для API-тестирования
- **Page Object Model (POM)** — паттерн проектирования

## Структура проекта

```
Marketplace/
├── api/                      # API клиенты и сервисы
│   ├── client.py            # Базовый API клиент
│   └── services/
│       └── user_api.py      # API эндпоинты пользователей
├── config/                   # Конфигурация
│   └── config.py            # Настройки приложения
├── pages/                    # Page Object Model
│   ├── base_page.py         # Базовый класс страницы
│   ├── home_page.py         # Главная страница
│   ├── login_page.py        # Страница входа
│   ├── registration_page.py # Страница регистрации
│   ├── contact_us_page.py   # Страница контактов
│   ├── products_page.py     # Страница товаров
│   └── cart_page.py         # Корзина
├── tests/                    # Тесты
│   ├── conftest.py          # pytest фикстуры
│   ├── test_login_page.py   # Тесты входа
│   ├── test_registration_page.py
│   ├── test_home_page.py
│   ├── test_contact_us_page.py
│   ├── test_products_page.py # Тесты страницы продуктов
│   └── test_cart_page.py    # Тесты корзины
├── utils/                    # Утилиты
│   └── data_generator.py    # Генератор тестовых данных
├── locators.py               # Все локаторы элементов
└── pytest.ini               # Конфигурация pytest
```

## Установка

```bash
pip install -r requirements.txt
```

## Запуск тестов

```bash
# Все тесты
pytest

# С детальным выводом
pytest -v

# Один тестовый файл
pytest tests/test_login_page.py

# Конкретный тест
pytest tests/test_login_page.py::TestLogin::test_login_user

# По маркеру
pytest -m smoke              # Только дымовые тесты
pytest -m ui                 # Только UI тесты
pytest -m positive           # Позитивные тесты
pytest -m negative           # Негативные тесты
```

## Переменные окружения

| Переменная | Описание | По умолчанию |
|------------|----------|--------------|
| BASE_URL | URL сайта | https://automationexercise.com |
| API_URL | URL API | https://automationexercise.com/api |
| HEADLESS | Запуск без UI | false |
| TIMEOUT | Таймаут ожидания | 10 |
| BROWSER | Браузер | chrome |

## Маркеры тестов

| Маркер | Описание |
|--------|----------|
| `register_user` | Регистрация нового пользователя |
| `login_user` | Авторизация пользователя |
| `ui` | UI тесты |
| `smoke` | Дымовые тесты |
| `positive` | Позитивные тесты |
| `negative` | Негативные тесты |
| `incorrect_login_user` | Вход с неверными данными |
| `register_exist_email` | Регистрация с существующим email |
| `contact_us` | Форма обратной связи |
| `view_product` | Просмотр карточки товара |
| `search_product` | Поиск товаров |
| `subscribe` | Подписка на рассылку |
| `subscribe_from_home` | Подписка на рассылку с главной страницы |
| `subscribe_from_cart` | Подписка на рассылку со страницы корзины |
