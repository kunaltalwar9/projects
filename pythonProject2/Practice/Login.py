from selenium import webdriver


class Login:
    text_email_xpath = ""
    text_password_xpath = ""
    button_signin_xpath = ""
    button_signout_xpath=""

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element_by_xpath(self.text_email_xpath).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_xpath(self.text_password_xpath).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_signin_xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_xpath(self.button_signout_xpath).click()
