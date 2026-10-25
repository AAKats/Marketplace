![CI](https://github.com/AAKats/Marketplace/actions/workflows/tests.yml/badge.svg)
[Allure-отчёт](https://aakats.github.io/Marketplace/)
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
│   ├── assertions.py        # Переиспользуемые функции проверок API
│   └── services/
│       ├── user_api.py      # API эндпоинты пользователей
│       └── products_api.py  # API эндпоинты продуктов
├── config/                   # Конфигурация
│   └── config.py            # Настройки приложения
├── pages/                    # Page Object Model
│   ├── base_page.py         # Базовый класс страницы
│   ├── cart_page.py         # Корзина
│   ├── checkout_page.py     # Оформление заказа
│   ├── contact_us_page.py   # Страница контактов
│   ├── login_page.py        # Страница входа
│   ├── payment_page.py      # Оплата
│   ├── product_page.py      # Карточка товара
│   ├── products_page.py     # Список товаров
│   └── registration_page.py # Страница регистрации
├── tests/                    # Тесты
│   ├── conftest.py          # pytest фикстуры
│   ├── test_products_api.py # API тесты продуктов
│   ├── test_user_api.py     # API тесты пользователей
│   ├── test_cart_page.py    # Тесты корзины и checkout
│   ├── test_contact_us_page.py
│   ├── test_login_page.py   # Тесты входа
│   ├── test_products_page.py
│   ├── test_product_page.py    # Тесты карточки товара
│   └── test_registration_page.py
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
pytest -m regress            # Только регрессионные тесты
pytest -m ui                 # Только UI тесты
pytest -m positive           # Позитивные тесты
pytest -m negative           # Негативные тесты

# Параллельный запуск (требуется pytest-xdist)
pytest -n auto               # Автоопределение числа потоков
pytest -n 4                  # Явно 4 потока
pytest -n 8 -v               # 8 потоков с детальным выводом

# Headless-режим (без окна браузера)
pytest --headless
```

Альтернативно можно задать env-переменную `HEADLESS=true` — оба способа эквивалентны.

## Allure-отчёты

```bash
# Запуск тестов с сохранением результатов Allure
pytest --alluredir=allure-results

# Просмотр отчёта в браузере
allure serve allure-results

# Генерация статического HTML-отчёта
allure generate allure-results -o allure-report --clean

# Открыть сгенерированный отчёт
allure open allure-report
```

> **Примечание:** Для работы Allure-отчётов требуется установленный [Allure CLI](https://allurereport.org/docs/install/).

## Переменные окружения

| Переменная | Описание | По умолчанию |
|------------|----------|--------------|
| BASE_URL | URL сайта | https://automationexercise.com |
| API_URL | URL API | https://automationexercise.com/api |
| HEADLESS | Запуск без UI (аналог опции `--headless`) | false |
| TIMEOUT | Таймаут ожидания | 10 |
| BROWSER | Браузер | chrome |

## Маркеры тестов

| Маркер     | Описание            |
|------------|---------------------|
| `ui`       | UI тесты            |
| `smoke`    | Дымовые тесты       |
| `regress`  | Регрессионные тесты |
| `positive` | Позитивные тесты    |
| `negative` | Негативные тесты    |
| `api`      | API тесты           |
