from selenium.webdriver.common.by import By


class UrlsAndLocators:
    default_browser = 'firefox'
    chrome_driver_path = r"C:\Users\Kunal Talwar\eclipse-workspace\libs\chromedriver_win32\chromedriver.exe"
    firefox_driver_path = r"C:\Users\Kunal Talwar\eclipse-workspace\libs\geckodriver-v0.31.0-win64\geckodriver.exe"
#    url = 'http://demostore.supersqa.com/'
#    add_to_cart_elements = "a[class='button product_type_simple add_to_cart_button ajax_add_to_cart']"
#    //a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart']//following-sibling::a
#    home_page_elements = (By.CSS_SELECTOR, add_to_cart_elements)
#    for element in home_page_elements:
#        print(element)

#    album = (By.CSS_SELECTOR, "a[data-product_sku='woo-album']")
#    beanie_with_logo = (By.CSS_SELECTOR, "a[data-product_sku='Woo-beanie-logo']")
#    long_sleeve_tee = (By.CSS_SELECTOR, "a[data-product_sku='woo-long-sleeve-tee']")
    album1 = "a[data-product_sku='woo-album']"
    beanie_with_logo1 = "a[data-product_sku='Woo-beanie-logo']"
    long_sleeve_tee1 = "a[data-product_sku='woo-long-sleeve-tee']"
    cart_link = 'http://demostore.supersqa.com/cart/'
    cart_btn = 'a[class="cart-contents"]'
    free_shipping_radio_on_cart = 'shipping_method_0_free_shipping2'
    coupon_field = 'coupon_code'
    apply_coupon_button = 'button[name="apply_coupon"]'
    proceed_to_checkout_on_cart = 'a[class="checkout-button button alt wc-forward"]'
    local_pickup_on_cart = 'shipping_method_0_local_pickup3'
    first_name = "billing_first_name"
    first_name1 = (By.ID, "billing_first_name")
    last_name = "billing_last_name"
    country_dropdown = 'span[id="select2-billing_country-container"]'
    street_address = 'billing_address_1'
    town_city = 'billing_city'
    zip_code = 'billing_postcode'
    phone_number = 'billing_phone'
    email_address = 'billing_email'
    place_order = 'place_order'







