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

    SUBSCRIPTION = (By.CSS_SELECTOR, '#footer h2')
    SUBSCRIBE_EMAIL_FORM = (By.ID, 'susbscribe_email')
    SUBSCRIBE_BUTTON = (By.ID, 'subscribe')
    SUCCESS_SUBSCRIBE_ALERT = (By.CLASS_NAME, 'alert-success')

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

class ProductsPageLocators:
    PRODUCTS_LIST = (By.CLASS_NAME, 'features_items')
    PRODUCT_NAMES = (By.CSS_SELECTOR, '.productinfo p')
    PRODUCT_PRICES = (By.CSS_SELECTOR, '.productinfo h2')
    VIEW_PRODUCT_BUTTONS = (By.CSS_SELECTOR, '.choose a')
    SEARCH_FIELD = (By.ID, 'search_product')
    SEARCH_BUTTON = (By.ID, 'submit_search')
    TITLE = (By.CSS_SELECTOR, '.title')
    ADD_TO_CART_BUTTONS = (By.CLASS_NAME, 'add-to-cart')
    CONTINUE_SHOPPING_BUTTON = (By.CLASS_NAME, 'close-modal')
    VIEW_CART_VIA_MODAL = (By.CSS_SELECTOR, 'a[href="/view_cart"]')


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product-information h2 ')
    CATEGORY = (By.XPATH, '//p[contains(text(), "Category:")]')
    PRICE = (By.CSS_SELECTOR, '.product-information > span > span')
    AVAILABILITY = (By.XPATH, '//b[contains(text(), "Availability:")]')
    CONDITION = (By.XPATH, '//b[contains(text(), "Condition:")]')
    BRAND = (By.XPATH, '//b[contains(text(), "Brand:")]')


class CartPageLocators:
    PRODUCTS_IN_CART = (By.CSS_SELECTOR, '[id*="product-"]')
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, '[id*="product-"] .cart_description a')
    PRODUCT_PRICE_IN_CART = (By.CSS_SELECTOR, '[id*="product-"] .cart_price p')
    PRODUCT_QUANTITY_IN_CART = (By.CSS_SELECTOR, '[id*="product-"] .cart_quantity button')
    PRODUCT_TOTAL_PRICE_IN_CART = (By.CSS_SELECTOR, '[id*="product-"] .cart_total p')
    DELETE_PRODUCT_IN_CART = (By.CSS_SELECTOR, '[id*="product-"] .cart_delete a')

