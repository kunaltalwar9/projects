from amazon.src.pages.locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from amazon.src.SeleniumExtended import SeleniumExtended
from amazon.src.helpers.config_helpers import get_base_url
import logging as logger


class MyAccountSignedOut(MyAccountSignedOutLocator):
    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        logger.info(f"Going to {my_account_url}")
        self.driver.get(my_account_url)
        # self.driver.get("http://demostore.supersqa.com/my-account/")
        # pass

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGIN_USER_NAME)).send_keys(username)
        # self.driver.find_element('id', self.login_field)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGIN_PASSWORD)).send_keys(password)
        # pass

    def click_login_button(self):
        logger.debug("CLicking login button.")
        self.sl.wait_and_click(self.LOGIN_BTN)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGIN_BTN)).click()
        # pass

    def wait_until_error_is_displayed(self, exp_err):
        self.sl.wait_until_element_contains_text(self.ERRORS_UL, exp_err)

    def input_register_email(self, email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, email)

    def input_register_password(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password)

    def click_register_button(self):
        logger.debug("CLicking Register button.")
        self.sl.wait_and_click(self.REGISTER_BTN)
