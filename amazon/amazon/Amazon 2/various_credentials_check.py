import time

from selenium.webdriver.common.by import By

from common_functions import COMMON_FUNCTIONS
from locators import Locators
import check_credentials


class VariousCredentials:

    def various_credentials(self):
        for r in range(2, 7):
            # for c in range(1, cols+1):
            # sheet.cell(r, c).value

            common = COMMON_FUNCTIONS()
            common.open_url("https://www.amazon.in/", )
            # clicking on sign in link
            common.click_with_css_selector(Locators.sign_in_link_on_home_page)
            time.sleep(1)
            username = check_credentials.readData(check_credentials.path, r, 1)
            password = check_credentials.readData(check_credentials.path, r, 2)
            common.input_text_with_css_selector(Locators.email_id_in_signin, username)
            time.sleep(0.5)
            # clicking on continue button
            common.click_with_css_selector(Locators.continue_button_in_signin)
            try:
                if common.return_driver().find_element(By.XPATH,
                                                       '//div[@class="a-alert-content"]/ul/li/span').text == "We cannot find an account with that email address":
                    print("Incorrect Email Id: " + username + " is Entered\n+++++++++++++++++++")
                    time.sleep(0.3)
                    common.return_driver().close()
                    continue

            except:
                print("Correct Email Id: " + username + " is Entered")
                # entering password
                common.input_text_with_css_selector(Locators.pasword_in_signin, password)
                # clicking on sign in button
                common.click_with_css_selector(Locators.sign_in_button_after_entering_email)
                time.sleep(1)
                try:
                    if common.return_driver().find_element(By.XPATH,
                                                           "//div[@id='auth-error-message-box']/div").text != "There was a problem":
                        print("But Incorrect Password is entered\n+++++++++++++++++++")
                        time.sleep(0.3)
                    common.return_driver().close()


                except:
                    print("and Successfully Logged in\n+++++++++++++++++++")
                    common.return_driver().close()
            continue


run = VariousCredentials()
run.various_credentials()
