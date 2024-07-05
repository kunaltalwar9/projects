# com.google.android.play.games
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

desired_caps = dict(
    deviceName='Galaxy M31',
    platformName='Android',
    udid = 'RZ8N70BZVMR',
    appPackage= "com.google.android.play.games",
    appActivity="com.google.android.apps.play.games.features.builtingames.PrebundledWebGameActivity",
)

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# actions = TouchAction(driver)
# wait = WebDriverWait(driver,25,poll_frequency=1)
time.sleep(2)
# driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Play Cricket"]').click()