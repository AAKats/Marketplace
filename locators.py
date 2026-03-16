from selenium.webdriver.common.by import By


class LoginPageLocators:
    '''Локаторы страницы авторизации и регистрации'''

    # Локаторы для добавления нового пользователя
    NEW_USER_TITLE = (By.CSS_SELECTOR, '.signup-form > h2')
    NAME_SIGN_UP_FIELD = (By.CSS_SELECTOR,'[data-qa="signup-name"]')
    EMAIL_SIGN_UP_FIELD = (By.CSS_SELECTOR,'[data-qa="signup-email"]')
    SIGN_UP_BUTTON = (By.CSS_SELECTOR,'[data-qa="signup-button"]')
    SIGN_UP_ERROR = (By.CSS_SELECTOR, '[action="/signup"] p')
    
    # Локаторы для авторизации
    LOGIN_TITLE = (By.CSS_SELECTOR, '.login-form > h2')
    EMAIL_LOGIN_FIELD = (By.CSS_SELECTOR,'[data-qa="login-email"]')
    PASSWORD_LOGIN_FIELD = (By.CSS_SELECTOR,'[data-qa="login-password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR,'[data-qa="login-button"]')
    LOGIN_ERROR = (By.CSS_SELECTOR,'[action="/login"] p')


class BasePageLocators:
    '''Локаторы основной страницы сайта'''

    # Локаторы для навигационной панели
    HOME_BUTTON = (By.XPATH, '//i[@class="fa fa-home"]/parent::*')
    PRODUCTS_BUTTON = (By.XPATH, '//i[@class="material-icons card_travel"]/parent::*')
    CART_BUTTON = (By.XPATH, '//i[@class="fa fa-shopping-cart"]/parent::*')
    SIGNUP_LOGIN_BUTTON = (By.XPATH, '//i[@class="fa fa-lock"]/parent::*')
    LOGGED_AS_TEXT = (By.XPATH, '//i[@class="fa fa-user"]/parent::*')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'a[href="/logout"]')
    DELETE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'a[href="/delete_account"]')
    CONTACT_US_BUTTON = (By.CSS_SELECTOR, 'a[href="/contact_us"]')

    # Локаторы для страницы удаления аккаунта
    DELETE_TITLE = (By.CSS_SELECTOR,'.title > b')
    DELETE_TEXT_1 = (By.CSS_SELECTOR, '.col-sm-9 p')
    DELETE_TEXT_2 = (By.CSS_SELECTOR, '.col-sm-9 > p:nth-child(3)')
    DELETE_CONTINUE_BUTTON = (By.CSS_SELECTOR, '[data-qa="continue-button"]')



class RegistrationPageLocators:
    '''Локаторы страницы регистрации'''

    # Локаторы для страницы после успешной регистрации
    ACCOUNT_CREATED_TITLE = (By.CSS_SELECTOR, '.title > b')
    CONTINUE_AFTER_SIGNUP_BUTTON = (By.CSS_SELECTOR, '[data-qa="continue-button"]')
    CONGRATILATIONS_TEXT = (By.CSS_SELECTOR, '.col-sm-9 p')
    CONGRATILATIONS_TEXT_2 = (By.CSS_SELECTOR, '.col-sm-9 p:nth-child(3)')

    # Локаторы основных данных о пользователе
    ACCOUNT_INFORMATION_TITLE = (By.CSS_SELECTOR,'.title > b')
    MR_RADIOBUTTON = (By.ID,'id_gender1')
    MRS_RADIOBUTTON = (By.ID,'id_gender2')
    NAME_FIELD = (By.ID,'name')
    EMAIL_FIELD = (By.ID,'email')
    PASSWORD_FIELD = (By.ID,'password')
    DAY_OF_BIRTH_LIST = (By.ID,'days')
    MONTH_OF_BIRTH_LIST = (By.ID,'months')
    YEAR_OF_BIRTH_LIST = (By.ID,'years')
    NEWSLETTER_CHECKBOX = (By.ID,'newsletter')
    OFFERS_CHECKBOX = (By.ID,'optin')

    # Локаторы дополнительных данных о пользователе
    FIRST_NAME_FIELD = (By.ID,'first_name')
    LAST_NAME_FIELD = (By.ID,'last_name')
    COMPANY_FIELD = (By.ID,'company')
    ADDRESS_FIELD = (By.ID,'address1')
    ADDRESS_2_FIELD = (By.ID,'address2')
    COUTNRY_LIST = (By.ID,'country')
    STATE_FIELD = (By.ID,'state')
    CITY_FIELD = (By.ID,'city')
    ZIPCODE_FIELD = (By.ID,'zipcode')
    MOBILE_NUMBER_FIELD = (By.ID,'mobile_number')

    #Локатор кнопки завершения регистрации
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, '[data-qa="create-account"]')

class ContactUsPageLocators:
    '''Локаторы страницы обратной связи'''

    CONTACT_US_TITLE = (By.CSS_SELECTOR, '.col-sm-12 > .title')
    CONTACT_US_TITLE_2 = (By.CSS_SELECTOR, '.col-sm-8 > .contact-form > .title')
    NOTE = (By.CSS_SELECTOR, '.col-sm-8 > .contact-form > div')
    CONTACT_US_TITLE_3 = (By.CSS_SELECTOR, '.col-sm-4 .title')
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alert-success')

    # Локаторы заполняемых полей
    NAME_FIELD = (By.CSS_SELECTOR, '[data-qa="name"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, '[data-qa="email"]')
    SUBJECT_FIELD = (By.CSS_SELECTOR, '[data-qa="subject"]')
    MESSAGE_FIELD = (By.CSS_SELECTOR, '[data-qa="message"]')
    UPLOAD_FILE = (By.NAME, 'upload_file')

    # Локаторы кнопок
    SUBMIT_BUTTON = (By.NAME, 'submit')
    HOME_BUTTON = (By.CLASS_NAME, 'fa-angle-double-left')




