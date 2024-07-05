from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from appium.options.android import UiAutomator2Options
import time
# Step 1 : Import Appium Service class
from appium.webdriver.appium_service import AppiumService

# Step 2 : Create object for Appium Service class
appium_service = AppiumService()

# Step 3 : Call Start method by using Appium Service class object
appium_service.start()

# Step 5 : To Call stop method by using Appium Service class object
appium_service.stop()


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '12'
desired_caps['deviceName'] = 'Galaxy M31'
desired_caps['app'] = ('C:/Users/Kunal Talwar/Downloads/Android_Appium_Demo.apk')
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723')

ele_id = driver.find_element(AppiumBy.ID, "com.skill2lead.appiumdemo:id/EnterValue")
ele_id.click()
print("Text on the Button ", ele_id.text)
print("Text on the Button ", ele_id.get_attribute("text"))
print("Content Des  of the Button ", ele_id.get_attribute("content-desc"))
ele_id.click()

time.sleep(2)

ele_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
ele_classname.send_keys("Skill2Lead")
time.sleep(2)
ele_classname.clear()
time.sleep(2)
ele_classname.send_keys("Skill2Lead")

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

ele = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ScrollView"))
ele.click()

ele = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                          'new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON12"))'))
"""actions = TouchAction(driver)
#actions.tap(None,700,1990,1)
actions.tap(ele,940,2400,1)
actions.long_press(ele,5)
actions.perform()"""

action = ActionChains(driver)

action.click_and_hold(ele).perform()

ele.click()
time.sleep(2)

ele = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                          'new UiScrollable(new UiSelector()).scrollIntoView(text("DRAGANDDROP"))'))
ele.click()

ele_kw = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ingvw"))

ele_lay = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/layout2"))

actions = TouchAction(driver)

actions.long_press(ele_kw).move_to(ele_lay).release().perform()

print("Device Width and Height : ", driver.get_window_size())
# out of print statement is :Device Width and Height :  {'width': 1440, 'height': 2621}
deviceSize = driver.get_window_size()
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']

######Right to Left#######
startx = screenWidth * 8 / 9
endx = screenWidth / 9
starty = screenHeight / 2
endy = screenHeight / 2

###### Left to Right    #######
startx2 = screenWidth / 9
endx2 = screenWidth * 8 / 9
starty2 = screenHeight / 2
endy2 = screenHeight / 2

actions = TouchAction(driver)
actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
time.sleep(2)
actions.long_press(None, startx2, starty2).move_to(None, endx2, endy2).release().perform()

driver.quit()


# For hybrid app automation

# For switching between two apps

driver.start_activity("app_package1", "app_activity1")
time.sleep(5)
driver.start_activity("app_package2","app_activity2")
time.sleep(5)
driver.quit()

# For parallel testing
# code from lecture 144 as written below
# pip install pytest-xdist
# in desired capabilities, systport(systemPort) and udId must be added for
# pytest -n<numprocesses>
# adb shell dumpsys window windows | grep-E 'mCurrentFocus'

def deviceDriver(deviceID,sysPort):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['platformVersion'] = '12'
    desired_caps['deviceName'] = 'Galaxy M31'
    desired_caps['udid'] = deviceID
    desired_caps['systemPort'] = sysPort
    desired_caps['app'] = ('C:/Users/Kunal Talwar/Downloads/Android_Appium_Demo.apk')
    desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
    desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

    options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723')

    return driver

def enterText(driver):
    ele_id = driver.find_element(AppiumBy.ID, "com.skill2lead.appiumdemo:id/EnterValue")
    ele_id.click()

    time.sleep(2)

    ele_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
    ele_classname.click()
    ele_classname.send_keys("Skill2Lead")
    time.sleep(2)

    driver.quit()


def test_deviceTest():
    d1 = deviceDriver('emulator-5554', 8200)
    d2 = deviceDriver('RZ8N70BZVMR',8201)

    enterText(d1)
    enterText(d2)