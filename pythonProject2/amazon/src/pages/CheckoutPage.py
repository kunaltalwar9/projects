from amazon.src.SeleniumExtended import SeleniumExtended
from amazon.src.pages.locators.CheckoutPageLocators import CheckoutPageLocators
# from amazon.src.pages.locators import CheckoutPageLocators, if import this will give TypeError : module() takes at
# most 2 arguments (3 given) error
from amazon.src.helpers.generic_helpers import generate_random_email_and_password


class CheckoutPage(CheckoutPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    # def input_billing_first_name(self, first_name=TestFName):
    def input_billing_first_name(self, first_name=None):
        first_name = first_name if first_name else 'AutomationFName'
        self.sl.wait_and_input_text(self.BILLING_FIRST_NAME_FIELD, first_name)

    def input_billing_last_name(self, last_name=None):
        last_name = last_name if last_name else 'AutomationLName'
        self.sl.wait_and_input_text(self.BILLING_LAST_NAME_FIELD, last_name)

    def input_billing_street_address_1(self, address_1=None):
        address_1 = address_1 if address_1 else '123 Main st.'
        self.sl.wait_and_input_text(self.BILLING_ADDRESS_1_FIELD, address_1)

    def input_billing_city(self, city=None):
        city = 'San Francisco' if not city else city
        self.sl.wait_and_input_text(self.BILLING_CITY_FIELD, city)

    def input_billing_zip(self, zip_code=None):
        zip_code = 94016 if not zip_code else zip_code
        self.sl.wait_and_input_text(self.BILLING_ZIP_FIELD, zip_code)

    def input_billing_phone_number(self, phone=None):
        phone = '4151111111' if not phone else phone
        self.sl.wait_and_input_text(self.BILLING_PHONE_FIELD, phone)

    def input_billing_email(self, email=None):
        if not email:
            rand_email = generate_random_email_and_password()
            email = rand_email['email']
        # email = 94016 if not email else email
        self.sl.wait_and_input_text(self.BILLING_EMAIL_FIELD, email)

    def fill_in_billing_info(self, f_name=None, l_name=None, street1=None, city=None, zip_code=None, phone=None, email=None):
        self.input_billing_first_name(first_name=f_name)
        self.input_billing_last_name(last_name=l_name)
        self.input_billing_street_address_1(address_1=street1)
        self.input_billing_city(city=city)
        self.input_billing_zip(zip_code=zip_code)
        self.input_billing_phone_number(phone=phone)
        self.input_billing_email(email=email)

    def click_place_order(self):
        self.sl.wait_and_click(self.PLACE_ORDER_BTN)
