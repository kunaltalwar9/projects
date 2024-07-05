import time
from Practice import Check
from selenium import webdriver
import pytest

@pytest.fixture
def openchrome(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\chromedriver_win32"
                                                  r"\chromedriver.exe")
        driver.maximize_window()
        #driver.back()
        #driver.refresh()
        time.sleep(1)
        driver.get("https://www.zales.com")
        Check.signin()
    elif browser == 'firefox':
        driver = webdriver.Firefox(
            executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\geckodriver-v0.30.0-win64\geckodriver.exe")
    else:
        driver = webdriver.Ie()# act as default browser if not opted for chrome, firefox
    return driver
# command line arguments= pytest -s -v pytest.py -- browser chrome
# pytest -s -v pytest.py -- browser firefox
# for parallel running, we can use the pytest-xdist,  pytest -s -v -n=2 pytest.py -- browser chrome, n=2 indicates number of browser to run parallel

def openfirefox():
    driver = webdriver.Firefox(
        executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\geckodriver-v0.30.0-win64\geckodriver.exe")
    driver.maximize_window()
    time.sleep(1)
    driver.get("https://www.zales.com")


# command line option through fixture command, for passing different values to test function
def pytest_adoption(parser):
    parser.adoption("")


@pytest.fixture()
def browser(request):
    return request.config.getoption("")


def pytest_configure(config):
    config.metadata['Project Name']=''
    config.metadata['Module Name']=''
    config.metadata['Tester']=''


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
#pytest -s -v -n=2 --html= Pathofreport pytest.py -- browser chrome