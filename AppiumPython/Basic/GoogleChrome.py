import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
'''

desired_caps = dict(
    deviceName='Galaxy M31',
    platformName='Android',
    browserName='Chrome',
    udid = 'RZ8N70BZVMR',
    appPackage= "com.android.chrome",
    appActivity="com.google.android.apps.chrome.Main",
    automationName = 'uiautomator2'
)
driver = webdriver.Remote('https://127.0.0.1:4723/wd/hub', desired_caps)

desired_cap2 = {
    "platformName": "Android",
    "deviceName": "Galaxy M31",
    "udid": "RZ8N70BZVMR",
    "app": "/Users/peri/Downloads/com.flipkart.android._2019-01-31.apk",
    "appPackage": "",
    "appWaitActivity":""
}

webdriver2 = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap2)

'''

'''
driver.get('https://www.google.com/maps')

# Search URL Tab in Chrome
driver.find_element(By.ID,'com.android.chrome:id/search_box_text')
driver.get("https:www.google.com/maps")
'''
# Correctly Working for Google Maps
'''
desired_caps = dict(
    deviceName='Galaxy M31',
    platformName='Android',
    udid = 'RZ8N70BZVMR',
    appPackage= "com.google.android.apps.maps",
    appActivity="com.google.android.maps.MapsActivity",
)

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(3)
driver.find_element(By.XPATH,'//android.widget.TextView[@text="Search here"]').click()
time.sleep(2)

driver.find_element(By.ID,'com.google.android.apps.maps:id/search_omnibox_edit_text').send_keys("ABC")
# Working till here

'''


# driver.find_element(By.XPATH,'//android.widget.TextView[@text="Search here"]').send_keys("ABC")
# driver.find_element(By.ID, "com.android.chrome:id/signin_fre_selected_account_expand_icon").click()

'''
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Galaxy M31'
desired_caps['udid'] = 'RZ8N70BZVMR'
desired_caps['appPackage'] = 'com.google.android.googlequicksearchbox'
desired_caps['appActivity'] = '.SearchActivity'

desired_caps = {'platformName': 'Android', 'deviceName': 'Galaxy M31', 'udid': 'RZ8N70BZVMR',
                'appPackage': 'com.google.android.googlequicksearchbox', 'appActivity': '.SearchActivity'}

'''


desired_caps = dict(
    deviceName='Galaxy M31',
    platformName='Android',
    udid = 'RZ8N70BZVMR',
    appPackage= "com.google.android.googlequicksearchbox",
    appActivity=".SearchActivity",
    # noReset = True
)

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
actions = TouchAction(driver)
wait = WebDriverWait(driver,25,poll_frequency=1)
time.sleep(2)
'''
# Tap Switch Profile
actions.tap(None,1000,150,1).perform()
time.sleep(1)

# webview = driver.contexts[0]
# driver.switch_to.context(webview)

# Tap Profile switch dropdown
actions.tap(None,950,500,1).perform()
time.sleep(3)
# Tap to Other Profile
actions.tap(None,200,1025,1).perform()
time.sleep(2)

driver.find_element(By.ID,'com.google.android.googlequicksearchbox:id/og_collapsed_chevron').is_displayed()
'''
# time.sleep(3)
# Google Search bar Click
# driver.find_element(By.ID, 'com.google.android.googlequicksearchbox:id/googleapp_hint_text').click()
wait.until(lambda  x: x.find_element(By.ID, 'com.google.android.googlequicksearchbox:id/googleapp_hint_text')).click()
# time.sleep(1)
# Google Input Maps Link
# driver.find_element(By.ID, 'com.google.android.googlequicksearchbox:id/googleapp_search_box').send_keys("https://www.google.com/maps/place/Pop+Tate's+Kurla/@19.0868264,72.88887,17z/data=!3m1!5s0x3be7c8878a6ce00d:0x5d860d2b775b3318!4m8!3m7!1s0x3be7c87d614aa151:0x9a254de49502ee62!8m2!3d19.0868264!4d72.88887!9m1!1b1!16s%2Fg%2F1thwyxfn?authuser=0&hl=en&entry=ttu")
# 1st Restaurant
# wait.until(lambda  x: x.find_element(By.ID, 'com.google.android.googlequicksearchbox:id/googleapp_search_box')).send_keys("https://www.google.com/maps/place/Pop+Tate's+Kurla/@19.0868264,72.88887,17z/data=!3m1!5s0x3be7c8878a6ce00d:0x5d860d2b775b3318!4m8!3m7!1s0x3be7c87d614aa151:0x9a254de49502ee62!8m2!3d19.0868264!4d72.88887!9m1!1b1!16s%2Fg%2F1thwyxfn?authuser=0&hl=en&entry=ttu")
# 2nd Restaurant
wait.until(lambda  x: x.find_element(By.ID, 'com.google.android.googlequicksearchbox:id/googleapp_search_box')).send_keys("https://goo.gl/maps/kGcWWA3G67GiXYhG8")
time.sleep(1)
# Press Enter
driver.press_keycode(66)
time.sleep(6)

print(driver.contexts)

# driver.find_element(By.XPATH,"//button[@aria-label='Reviews for Trèsind Mumbai']/div[2]").click()
'''
# Tap on Review Section
actions.tap(None,600,307,1).perform()
time.sleep(2)
# Overall Five Star
actions.tap(None,750,1300,1).perform()
# Food
actions.tap(None,970,580,1).perform()
# Service
actions.tap(None,970,750,1).perform()
# Atmosphere
actions.tap(None,970,910,1).perform()

driver.find_element(By.ID,'com.google.android.apps.maps:id/contentEditText').send_keys("ABC")
# driver.save_screenshot()
# Post
actions.tap(None,500,2110,1).perform()

driver.close()

'''