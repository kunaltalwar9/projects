import pytest
from amazon.src.pages.MyAccountSignedIn import MyAccountSignedIn
from amazon.src.pages.MyAccountSignedOut import MyAccountSignedOut
from amazon.src.helpers.generic_helpers import generate_random_email_and_password


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:
    @pytest.mark.tcid13
    def test_register_valid_new_user(self):
        my_account_o = MyAccountSignedOut(self.driver)
        my_account_o.go_to_my_account()
        my_account_i = MyAccountSignedIn(self.driver)
        # go to my account
        # fill in email
        rand_email = generate_random_email_and_password()
        my_account_o.input_register_email(rand_email["email"])
        # fill in password
        my_account_o.input_register_password('abcd123')
        # click register
        my_account_o.click_register_button()
        # verify user is registered
        my_account_i.verify_user_is_signed_in()
