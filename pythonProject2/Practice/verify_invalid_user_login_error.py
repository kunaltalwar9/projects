from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InvalidUserLoginError:
    invalid_email = 'abc@outlook.com'
    invalid_password = 'abcabc'
    url = 'http://demostore.supersqa.com/my-account/'
    expected_msg = 'Unknown email address. Check again or try your username.'

    def __init__(self):
        self.driver = webdriver.Firefox(
            executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\geckodriver-v0.30.0-win64\geckodriver.exe")
        self.driver.implicitly_wait(10)
        time.sleep(2)

    def go_to_my_account(self):
        self.driver.get(self.url)

    def input_email(self):
        field = self.driver.find_element(By.ID, 'username')
        field.send_keys(self.invalid_email)

    def input_password(self):
        field = self.driver.find_element(By.ID, 'password')
        field.send_keys(InvalidUserLoginError.invalid_password)

    def click_login(self):
        self.driver.find_element(By.NAME, 'login').click()

    def verify_error_message(self):
        err_elm = self.driver.find_element(By.CSS_SELECTOR, "div[class='woocommerce'] ul li")
        displayed_mrr = err_elm.text
        assert displayed_mrr == self.expected_msg, 'The displayed error msg is not expected'
        print("PASS")

    def main(self):
        self.go_to_my_account()
        self.input_email()
        self.input_password()
        time.sleep(2)
        self.click_login()
        self.verify_error_message()
        #self.driver.quit()


if __name__ == '__main__':
    obj = InvalidUserLoginError()
    obj.main()
