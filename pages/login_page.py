from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Локаторы для login_page
    NAME_SIGN_UP_FIELD = (By.CSS_SELECTOR,'data-qa="signup-name"')
    EMAIL_SIGN_UP_FIELD = (By.CSS_SELECTOR,'data-qa="signup-email"')