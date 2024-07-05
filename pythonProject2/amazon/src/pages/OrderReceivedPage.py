from amazon.src.SeleniumExtended import SeleniumExtended
from amazon.src.pages.locators.OrderReceivedPageLocators import OrderReceivedPageLocators


class OrderReceivedPage(OrderReceivedPageLocators):  # class OrderReceivedPage()

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_order_received_page_loaded(self):
        self.sl.wait_until_element_contains_text(self.PAGE_MAIN_HEADER, 'Order received')  #self.sl.wait_until_element_contains_text(OrderReceivedPageLocators.PAGE_MAIN_HEADER, )

    def get_order_number(self):
        self.sl.wait_and_get_text(self.ORDER_NUMBER)



