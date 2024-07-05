from selenium import webdriver
from amazon.check1.urls_and_locators import UrlsAndLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class CommonFunctions(UrlsAndLocators):

    # def __init__(self):
    #    driver = self.return_driver()
    # def __init__(self, driver):
    #    driver = self.return_driver()
    #    self.driver = driver
    # def __init__(self):
    #    driver = self.return_driver()
    #    return driver
    # def __init__(self):
    #    self.driver = webdriver.Firefox(executable_path=self.firefox_driver_path)
    def __init__(self):
        self.driver = self.return_driver()

    def which_browser(self, browser=None):
        browser = browser if browser else self.default_browser
        if browser == 'firefox':
            return webdriver.Firefox(executable_path=self.firefox_driver_path)
        elif browser == 'chrome':
            return webdriver.Chrome(executable_path=self.chrome_driver_path)

    def return_driver(self, browser=None):
        browser = browser if browser else self.default_browser
        webdriver_value = self.which_browser(browser)
        return webdriver_value

    #    def which_url(self, browser, url):
    #        driver = self.which_browser(browser)
    #        driver.get(url)

    def which_url2(self, url, browser=None):
        browser = browser if browser else self.default_browser
        driver = self.return_driver(browser)
        driver.get(url)
        # return driver

    def which_url3(self, url, browser=None):
        # browser = browser if browser else self.default_browser
        # driver = self.return_driver(browser)
        self.driver.get(url)

    '''    def add_to_cart(self, item1, item2):
            #CommonFunctions.driver(self, 'firefox')
            driver = self.return_driver()
            driver.find_element(By.CSS_SELECTOR, item1).click()
            driver.find_element(By.CSS_SELECTOR, item2).click()
            #item1.click()
    '''

    def add_to_cart2(self, item1, item2, item3):
        # CommonFunctions.driver(self, 'firefox')
        # cf = CommonFunctions()
        # driver = self.return_driver('firefox')
        self.driver.find_element(By.CSS_SELECTOR, item1).click()
        self.driver.find_element(By.CSS_SELECTOR, item2).click()
        self.driver.find_element(By.CSS_SELECTOR, item3).click()
        # self.driver.find_element(item1).click()
        # self.driver.find_element(item2).click()
        # self.driver.find_element(item3).click()
        # item1.click()

    def click_with_css_locator(self, locator):
        self.driver.find_element(By.CSS_SELECTOR, locator).click()
        # CommonFunctions.locate_element_via_css_selector(locator).click()
        # self.locate_element_via_css_selector(locator).click()

    def click_with_id_locator(self, locator):
        self.driver.find_element(By.ID, locator).click()

    def locate_element_via_css_selector(self, locator):
        self.driver.find_element(By.CSS_SELECTOR, locator)
        # return self.driver.find_element(By.CSS_SELECTOR, locator)

    #    @staticmethod
    #    def locate_element_via_css_selector1(locator):
    # return CommonFunctions.driver.find_element(By.CSS_SELECTOR, locator)

    def input_text_field(self, locator, text):
        self.driver.find_element((locator)).send_keys(text)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def input_text_field_with_id(self, locator, text):
        self.driver.find_element(By.ID, locator).send_keys(text)

    # @staticmethod
    def select_element(self, locator):
        select = Select(locator)
        select.select_by_value('United States (US)')
