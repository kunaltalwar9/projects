import time
from common_functions import COMMON_FUNCTIONS
from locators import Locators


common = COMMON_FUNCTIONS()
common.open_url("https://www.amazon.in/", )
# clicking on sign in link
common.click_with_css_selector(Locators.sign_in_link_on_home_page)
time.sleep(1)
# adding email id
common.input_text_with_css_selector(Locators.email_id_in_signin, "kunaltalwarthegreat@gmail.com")
time.sleep(0.5)
# clicking on continue button
common.click_with_css_selector(Locators.continue_button_in_signin)
# entering password
common.input_text_with_css_selector(Locators.pasword_in_signin, "Pass@123")
# clicking on sign in button
common.click_with_css_selector(Locators.sign_in_button_after_entering_email)
assert common.return_driver().title == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
time.sleep(1)
# common.input_text_with_css_selector(Locators.pasword_in_signin,"Pass@123")
# time.sleep(5)
# common.click_with_css_selector(Locators.sign_in_button_after_entering_email)
# common.click_with_css_selector(Locators.second_continue_button)
# time.sleep(15)
# common.click_with_css_selector(Locators.submit_code_button)
# time.sleep(1)
# search text
common.input_text_with_css_selector(Locators.search_text_box,"Halter Dress")
common.click_with_css_selector(Locators.search_icon)
common.scroll_by()

price_list = common.find_elements_by_css(Locators.all_products_price)
for i in price_list:
    print(i.text)

