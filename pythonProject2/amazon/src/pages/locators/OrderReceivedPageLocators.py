from selenium.webdriver.common.by import By


class OrderReceivedPageLocators:
    PAGE_MAIN_HEADER = (By.CSS_SELECTOR, "header h1.entry-title")  # main article header h1
    ORDER_NUMBER = (By.CSS_SELECTOR, 'li.order strong')  # .woocommerce-order-overview__order strong
