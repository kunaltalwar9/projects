import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# Telegram
driver = webdriver.Firefox()
driver.get("https://web.telegram.org/a/")
time.sleep(12)

driver.find_element(By.CSS_SELECTOR,"#telegram-search-input").click()
driver.find_element(By.CSS_SELECTOR,"#telegram-search-input").send_keys("You")

# Instagram
driver.execute_script("window.open('https://www.instagram.com/')")
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.CSS_SELECTOR,".xseo6mj > div:nth-child(1) > i:nth-child(1)").click()
# Email
driver.find_element(By.CSS_SELECTOR,"input[name='username']").click()
driver.find_element(By.CSS_SELECTOR,"input[name='username']").send_keys("rohansahai1993@gmail.com")
time.sleep(1)
# Password
driver.find_element(By.CSS_SELECTOR,"input[name='password']").click()
driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("Rohan@1993")
time.sleep(1)
# Login
driver.find_element(By.CSS_SELECTOR,"div.x1xmf6yo:nth-child(3)").click()
time.sleep(4)
# User Account
driver.get("https://www.instagram.com/sumandhanuk2709/")
time.sleep(4)
# Follow
driver.find_element(By.CSS_SELECTOR,"._aacw").click()

# Google
driver.execute_script("window.open('https://accounts.google.com/v3/signin/identifier?ifkv=ASKXGp0-EHTzolo151Bl2774CmVFZCBinKJsO3NuHGs4XVO46rt5f8qJu5hOUYrRJ30c5HqpeMK0&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S202119202%3A1706261998245226&theme=glif')")
time.sleep(2)
driver.switch_to.window(driver.window_handles[2])
# Email
driver.find_element(By.ID, "identifierId").click()
driver.find_element(By.ID, "identifierId").send_keys("rohansahai1993@gmail.com")




