# go to homepage
# add 1 item to cart
# go to cart
# apply free coupon
# select free shipping
# click on checkout
# fill in form
# click on place order
# verify order received
# verify order is recorded in db via SQL or via API
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from selenium.webdriver.common.by import By
from amazon.check1.urls_and_locators import UrlsAndLocators
from amazon.check1.common_functions import CommonFunctions
import time


class Check1(UrlsAndLocators, CommonFunctions):
    url = 'http://demostore.supersqa.com/'
    check1 = CommonFunctions()
    # open browser with specific url to reach homepage
    check1.which_url3(url=url)
    time.sleep(2)
    urls1 = UrlsAndLocators()
    #    check1.add_to_cart(urls1.album, urls1.beanie_with_logo)
    #    check1.add_to_cart2(urls1.album, urls1.beanie_with_logo, urls1.long_sleeve_tee)
    # add items to cart
    check1.add_to_cart2(urls1.album1, urls1.beanie_with_logo1, urls1.long_sleeve_tee1)
    #    driver = check1.return_driver('firefox')
    #    driver.find_element(By.CSS_SELECTOR, urls1.album1).click()
    # click on cart
    check1.click_with_css_locator(urls1.cart_btn)
    check1.driver.find_element(By.CSS_SELECTOR, urls1.cart_btn).click()
    check1.driver.refresh()

    # apply free coupon left
    check1.input_text_field_with_id(urls1.coupon_field, 'SSQA100')
    check1.click_with_css_locator(urls1.apply_coupon_button)
    # select free shipping
    try:
        check1.click_with_id_locator(urls1.free_shipping_radio_on_cart)
    except:
        check1.click_with_id_locator(urls1.local_pickup_on_cart)
    time.sleep(2)
    # click on checkout
    check1.click_with_css_locator(urls1.proceed_to_checkout_on_cart)
    # fill in form
    check1.input_text_field_with_id(urls1.first_name, 'Andre')
    check1.input_text_field_with_id(urls1.last_name, 'Nesta')
    # check1.select_element(By.CSS_SELECTOR, urls1.country_dropdown)
    check1.input_text_field_with_id(urls1.street_address, 'Antonio, Parma')
    check1.input_text_field_with_id(urls1.town_city, 'Parma')
    check1.input_text_field_with_id(urls1.zip_code, '11111')
    check1.input_text_field_with_id(urls1.phone_number, '+1234567891')
    check1.input_text_field_with_id(urls1.email_address, 'abcd@test.com')
    time.sleep(2)
    check1.click_with_id_locator(urls1.local_pickup_on_cart)
    time.sleep(2)
    check1.click_with_id_locator(urls1.place_order)

# selenium.common.exceptions.StaleElementReferenceException: Message: The element reference of <a
# class="cart-contents" href="http://demostore.supersqa.com/cart/"> is stale; either the element is no longer
# attached to the DOM, it is not in the current frame context, or the document has been refreshed Stacktrace: --
# selenium.common.exceptions.InvalidArgumentException: Message: expected value at line 1 column 11
# selenium.common.exceptions.ElementClickInterceptedException: Message: Element <button id="place_order"
# class="button alt" name="woocommerce_checkout_place_order" type="submit"> is not clickable at point (952,
# 618) because another element <div class="blockUI blockOverlay"> obscures it Stacktrace:
# TypeError 'NoneType' is not iterable
