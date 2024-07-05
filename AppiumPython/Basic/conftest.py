# Packages Base, Utilities, Pages, Configuration Files, Tests, Screenshots, Reports
# Foundation Sprints, Building Sprints, Firm-up Sprints, Nexus Framework, Scaling Agile Framework, Large Scale Scrum

import pytest
# conftest.py file name for all common functions
from allure_commons._allure import attach


@pytest.yield_fixture(scope='module')
def beforeClass():
    print('Before Class')
    yield
    print('After Class')

@pytest.yield_fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')

def test_methodA(beforeClass,beforeMethod):
    print("This is method A")

def test_methodB(beforeClass,beforeMethod):
    print("This is method B")

# pip3 install pytest-ordering
print("This is a Run Order class")

@pytest.mark.run(order=4)
def test_methodA():
    print("This is method A")

@pytest.mark.run(order=3)
def test_methodB():
    print("This is method B")

@pytest.mark.run(order=1)
def test_methodC():
    print("This is method C")

@pytest.mark.run(order=2)
def test_methodD():
    print("This is method D")

# pip install pytest-rerunfailures
# py.test --reruns 5 --reruns delay 2 filename.py # to rerun same file 5 times, with delay of 2 seconds
# if it passes it will rerun only 1 time

# other way

@pytest.mark.flaky(reruns=5)
def test_abc():
    pass

    from appium import webdriver
    from appium.webdriver.common.appiumby import AppiumBy
    import time
    import pytest

    @pytest.mark.flaky(reruns=5)
    def test_runAppiumTest():
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformVersion'] = '11'
        desired_caps['deviceName'] = 'Pixel3XL'
        desired_caps['app'] = ('/Users/sujithreddy/Documents/Code2Lead/Others/kwad.apk')
        desired_caps['appPackage'] = 'com.code2lead.kwad'
        desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        attach(data=self.driver.get_screenshot_as_png())

        ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValu")
        ele_id.click()

        time.sleep(5)

        driver.quit()