from selenium.webdriver.common.by import By


class MyAccountSignedOutLocator:
    # LOGIN_USER_NAME = (By.CSS_SELECTOR, 'input[id="ap_email"]')
    #  LOGIN_PASSWORD = (By.ID, 'ap_password')
    #  LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[id="signInSubmit"]')

    LOGIN_USER_NAME = (By.ID, 'username')
    LOGIN_PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[value="Log In"]')
    ERRORS_UL = (By.CSS_SELECTOR, 'ul.woocommerce-error')
    REGISTER_EMAIL = (By.ID, 'reg_email')
    REGISTER_PASSWORD = (By.ID, 'reg_password')
    REGISTER_BTN = (By.CSS_SELECTOR, 'button[value="Register"]')
