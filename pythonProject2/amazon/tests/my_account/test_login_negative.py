import pytest
from amazon.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures('init_driver')
class TestLoginNegative:
    @pytest.mark.tcid12
    def test_login_none_existing_user(self):
        print(" *******\n", "TEST LOGIN NON EXISTING\n", "********")
        # pytest - m tcid12 -s --log-cli-level= DEBUG
        my_account = MyAccountSignedOut(self.driver)
        # go to my account
        my_account.go_to_my_account()
        # type username
        my_account.input_login_username('asfsadf@g')
        # type password
        my_account.input_login_password('hgfdhfnh')
        # click login
        my_account.click_login_button()
        # verify error message
        expected_err = 'Error: The username asfsadf@g is not registered on this site. If you are unsure of your username, try your email address instead.'
        my_account.wait_until_error_is_displayed(expected_err)
