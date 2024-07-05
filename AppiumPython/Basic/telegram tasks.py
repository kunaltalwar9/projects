import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException


all_restaurants_list =["https://www.google.com/maps/place/Pop+Tate's+Kurla/@19.0868264,72.88887,17z/data=!3m1!5s0x3be7c8878a6ce00d:0x5d860d2b775b3318!4m8!3m7!1s0x3be7c87d614aa151:0x9a254de49502ee62!8m2!3d19.0868264!4d72.88887!9m1!1b1!16s%2Fg%2F1thwyxfn?authuser=0&hl=en&entry=ttu",
                       "https://goo.gl/maps/MeESwWu5VjMFrhdi9", "https://goo.gl/maps/JHwaP4mUqRQmryBZA","https://goo.gl/maps/kGcWWA3G67GiXYhG8","https://goo.gl/maps/uaei9CeoGMCixSK68","https://goo.gl/maps/xsUgo3dpJHezAPPP6"]

# "https://goo.gl/maps/MeESwWu5VjMFrhdi9", "https://goo.gl/maps/JHwaP4mUqRQmryBZA",

for i in range(0,len(all_restaurants_list)):
    desired_caps = dict(
        deviceName='Galaxy M31',
        platformName='Android',
        udid='RZ8N70BZVMR',
        appPackage="com.google.android.googlequicksearchbox",
        appActivity=".SearchActivity",
    )

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    actions = TouchAction(driver)
    wait = WebDriverWait(driver, 25, poll_frequency=1)
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
    # driver.find_element(By.ID, 'com.google.android.googlequicksearchbox:id/googleapp_hint_text').click()
    wait.until(
        lambda x: x.find_element(By.ID, 'com.google.android.googlequicksearchbox:id/googleapp_hint_text')).click()
    # time.sleep(1)
    # driver.find_element(By.ID, 'com.google.android.googlequicksearchbox:id/googleapp_search_box').send_keys("https://www.google.com/maps/place/Pop+Tate's+Kurla/@19.0868264,72.88887,17z/data=!3m1!5s0x3be7c8878a6ce00d:0x5d860d2b775b3318!4m8!3m7!1s0x3be7c87d614aa151:0x9a254de49502ee62!8m2!3d19.0868264!4d72.88887!9m1!1b1!16s%2Fg%2F1thwyxfn?authuser=0&hl=en&entry=ttu")
    # 1st Restaurant
    # wait.until(lambda  x: x.find_element(By.ID, 'com.google.android.googlequicksearchbox:id/googleapp_search_box')).send_keys("https://www.google.com/maps/place/Pop+Tate's+Kurla/@19.0868264,72.88887,17z/data=!3m1!5s0x3be7c8878a6ce00d:0x5d860d2b775b3318!4m8!3m7!1s0x3be7c87d614aa151:0x9a254de49502ee62!8m2!3d19.0868264!4d72.88887!9m1!1b1!16s%2Fg%2F1thwyxfn?authuser=0&hl=en&entry=ttu")
    # 2nd Restaurant
    wait.until(
        lambda x: x.find_element(By.ID, 'com.google.android.googlequicksearchbox:id/googleapp_search_box')).send_keys(all_restaurants_list[i])

    time.sleep(1)
    driver.press_keycode(66)
    time.sleep(5)
    # Tap on Review Section
    actions.tap(None, 600, 307, 1).perform()
    time.sleep(2)
    # Overall Five Star
    actions.tap(None, 750, 1300, 1).perform()
    '''
    try:
        actions.tap(None, 750, 1300, 1).perform()
        try:
        # Food Click
            driver.find_element(By.XPATH,
                            '(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/star5"])[2]').click()
            driver.find_element(By.XPATH,
                            '(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/star5"])[3]').click()
            driver.find_element(By.XPATH,
                            '(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/star5"])[4]').click()

        except:
            actions.tap(None, 800, 290, 1).perform()
            time.sleep(1)
            actions.tap(None, 735, 1440, 1).perform()
            time.sleep(2)
            # driver.find_element(By.XPATH,'//android.widget.ImageButton[@content-desc="Back"]').click()
            driver.find_element(By.XPATH,
                            '(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/star5"])[2]').click()
            driver.find_element(By.XPATH,
                            '(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/star5"])[3]').click()
            driver.find_element(By.XPATH,
                            '(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/star5"])[4]').click()
    except:
        actions.tap(None, 735, 1440, 1).perform()
        driver.find_element(By.XPATH,
                            '(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/star5"])[2]').click()
        driver.find_element(By.XPATH,
                            '(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/star5"])[3]').click()
        driver.find_element(By.XPATH,
                            '(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/star5"])[4]').click()
'''
    try:
    # Food Click
        driver.find_element(By.XPATH, '(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/star5"])[2]').click()
        driver.find_element(By.XPATH, '(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/star5"])[3]').click()
        driver.find_element(By.XPATH, '(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/star5"])[4]').click()

    except NoSuchElementException:
        actions.tap(None, 800, 290, 1).perform()
        time.sleep(1)
        actions.tap(None, 735, 1440, 1).perform()
        time.sleep(2)
    #    driver.find_element(By.XPATH,'//android.widget.ImageButton[@content-desc="Back"]').click()
        driver.find_element(By.XPATH,'(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/star5"])[2]').click()
        driver.find_element(By.XPATH,'(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/star5"])[3]').click()
        driver.find_element(By.XPATH,'(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/star5"])[4]').click()

    # driver.save_screenshot()
    # Post
    actions.tap(None, 500, 2110, 1).perform()
    time.sleep(7)