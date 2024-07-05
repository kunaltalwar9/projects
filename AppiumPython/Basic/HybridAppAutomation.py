from appium import webdriver
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

"""
1.) Mobile Browser version and ChromeDriver or respective Browser Driver should be in same version 
2.) 
Two Ways of Identifying locators on webview i) open chrome browser and type "chrome://inspect/#devices" ii) Use Browser 
inspectors 

"""
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel'
desired_caps['app'] = ('/Users/sujithreddy/Documents/Code2Lead/Others/kwad.apk')
desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'
desired_caps['noReset'] = True


# 1. Create the Driver object
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

print("Current Activity",driver.current_activity)
print("Current context",driver.current_context)
print("Current orientation",driver.orientation)
print("Check Whether device is locked or not :",driver.is_locked())

# 2. Create WebDriverWait
wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

# 3. Open the URL in Browser
ele = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/terms_accept"))
ele.click()

ele2 = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/negative_button"))
ele2.click()

ele3 = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/search_box_text"))
ele3.click()

ele4 = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/url_bar"))
ele4.click()
ele4.send_keys("https://www.google.com/")

driver.press_keycode(66)

time.sleep(5)

# 4. Get the list of Contexts in App
appContexts = driver.contexts
print("AppContexts : ", appContexts)

# 5. switch to webview to perform action on Required URL or on WebView
for appType in appContexts:
    if appType == "WEBVIEW_chrome":
        driver.switch_to.context(appType)

# 6. Do testing on Webview screen in chrome browser or any if we want
ele4 = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//*[@name='q']"))
ele4.send_keys("Skill2Lead")

# 7. Switch back to native view to perform action
for appType in appContexts:
    if appType == "NATIVE_APP":
        driver.switch_to.context(appType)

# 8. Do testing on native app screen if we want

ele4 = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/url_bar"))
ele4.click()
ele4.send_keys("https://www.skill2lead.com/")
driver.press_keycode(66)

# 9. Quit or close the driver object

time.sleep(5)
driver.quit()


print("Is Displayed : ",ele.is_displayed())
print("Is Enabled : ",ele.is_enabled())
print("Is selected : ",ele.is_selected())
print("Size : ",ele.size)
print("Location : ",ele.location)

print("Text on the Button ", ele.text)
print("Text on the Button ", ele.get_attribute("text"))
print("Content Des  of the Button ", ele.get_attribute("content-desc"))

# To Scroll to a button having text locator value = Button12

ele = wait.until(lambda  x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                           'new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON12"))'))
ele.click()

# To long press
actions = TouchAction(driver)
# Try this, may work
actions.long_press(ele,duration=5).perform()
# As per code it is
actions.long_press(ele,5)
actions.perform()

# to Drag and drop
ele_kw = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ingvw"))
ele_lay = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/layout2"))
actions = TouchAction(driver)
actions.long_press(ele_kw).move_to(ele_lay).release().perform()

# To Swipe Right Left
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

###### Swipe from Bottom to Top  #######
startx = screenWidth / 2
endx = screenWidth / 2
starty = screenHeight * 8 / 9
endy = screenHeight / 9

###### Swipe from Top to Bottom #######
startx2 = screenWidth / 2
endx2 = screenWidth / 2
starty2 = screenHeight * 2 / 9
endy2 = screenHeight * 8 / 9

actions = TouchAction(driver)
actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
time.sleep(2)
actions.long_press(None, startx2, starty2).move_to(None, endx2, endy2).release().perform()