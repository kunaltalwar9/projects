from selenium import webdriver
import requests
import pytest
import os
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFOptions

@pytest.fixture(scope="class")
def init_driver(request):

    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff', 'headlessfirefox']
    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception('The environment variable BROWSER must be set')
    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f'Provided browser {browser} is not one of the supported browser.'
                        f'Supported browsers are {supported_browsers}')

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome(executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\chromedriver_win32"
                                                  r"\chromedriver.exe")
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox(
            executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\geckodriver-v0.30.0-win64\geckodriver.exe")
    elif browser in ('headlesschrome'):
        chrome_options = ChOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == 'headlessfirefox':
        ff_options = FFOptions()
        ff_options.add_argument('--disable-gpu')
        ff_options.add_argument('--no-sandbox')
        ff_options.add_argument('--headless')
        driver = webdriver.Firefox(options=ff_options)

    request.cls.driver = driver
    yield
    driver.quit()
