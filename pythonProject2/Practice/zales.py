from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
import click
import time

driver= webdriver.Firefox(
    executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\geckodriver-v0.30.0-win64\geckodriver.exe")
a = Alert(driver)
driver.get("https://www.zales.com/")
time.sleep(6)

try:
    alert = driver.switch_to.alert
    alert.dismiss()
except:
    driver.refresh()

driver.quit()

