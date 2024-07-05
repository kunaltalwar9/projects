from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class COMMON_FUNCTIONS:

    def __init__(self):
        self.driver = webdriver.Firefox(
            executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\geckodriver-v0.30.0-win64\geckodriver.exe")
        self.driver.maximize_window()
        # yield
        # driver.close()

    def open_url(self, url):
        self.driver.get(url)
        time.sleep(2)

    def click_with_css_selector(self, css_selector):
        self.driver.find_element(By.CSS_SELECTOR, css_selector).click()

    def input_text_with_css_selector(self, css_selector, input_text):
        self.driver.find_element(By.CSS_SELECTOR, css_selector).send_keys(input_text)

    def scroll_by(self):
        self.driver.execute_script("window.scrollBy(0,500)","")

    def find_elements_by_css(self,css_selector):
        return self.driver.find_elements(By.CSS_SELECTOR,css_selector)

    def return_driver(self):
        return self.driver
