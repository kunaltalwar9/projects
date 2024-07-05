import pytest
from selenium import webdriver
import time
class test_Browser:
    @pytest.fixture(scope='Class')
    def test_browser(self):
        driver = webdriver.Chrome(executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\chromedriver_win32"
                                                  r"\chromedriver.exe")
        driver.maximize_window()
        time.sleep(1)
        driver.get("https://www.amazon.com")
        yield
        driver.close()


