import os

class Config:
    # --- Окружение (Environment) ---
    # Получаем URL из переменных системы, или берем дефолтный, если не задано
    BASE_URL = os.getenv("BASE_URL", "https://automationexercise.com")
    API_URL = os.getenv("API_URL", "https://automationexercise.com/api")

    # --- Настройки UI (Browser & UI) ---
    # chrome, firefox, edge
    BROWSER = os.getenv("BROWSER", "chrome") 
    # Запуск без графического интерфейса
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    
    # Тайм-аут для явных ожиданий
    TIMEOUT = int(os.getenv("TIMEOUT", 10))
    
    # Разрешение экрана
    WINDOW_WIDTH = 1920
    WINDOW_HEIGHT = 1080

