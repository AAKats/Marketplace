from selenium.webdriver.common.by import By

class LoginPageLocators():
    # Локаторы для добавления нового пользователя
    NAME_SIGN_UP_FIELD = (By.CSS_SELECTOR,'data-qa="signup-name"')
    EMAIL_SIGN_UP_FIELD = (By.CSS_SELECTOR,'data-qa="signup-email"')
    SIGN_UP_BUTTON = (By.CSS_SELECTOR,'data-qa="signup-name"')
    # Локаторы для авторизации
    EMAIL_LOGIN_FIELD = (By.CSS_SELECTOR,'data-qa="login-email"')
    PASSWORD_LOGIN_FIELD = (By.CSS_SELECTOR,'data-qa="login-name"')
    LOGIN_BUTTON = (By.CSS_SELECTOR,'data-qa="login-name"')

class HomePageLocators():
    # Локаторы перехода по страницам сайта в навигации
    HOME_BUTTON = (By.XPATH, '//i[@class="fa fa-home"]/parent::*')
    PRODUCTS_BUTTON = (By.XPATH, '//i[@class="material-icons card_travel"]/parent::*')
    CART_BUTTON = (By.XPATH, '//i[@class="fa fa-shopping-cart"]/parent::*')
    SIGNUP_LOGIN_BUTTON = (By.XPATH, '//i[@class="fa fa-lock"]/parent::*')