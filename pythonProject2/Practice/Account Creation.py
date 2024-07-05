import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#id = "email"
xpath = '//*[@id="email"]'
driver = webdriver.Firefox(executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\geckodriver-v0.30.0-win64\geckodriver.exe")
driver.get("https://account.proton.me/signup")
time.sleep(4)
#driver.find_element(By.ID, id).send_keys("ABC")
driver.find_element(By.XPATH,'//div[@class="desktop"]/div/div/div/div/input[1]').send_keys("AC")

