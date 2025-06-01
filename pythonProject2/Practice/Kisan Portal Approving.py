import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()

driver.get("https://fasalrin.gov.in/")
# Click on Users Dropdown
driver.find_element(By.XPATH,"//div[@class='left-icon bottom-left']/div[1]").click()
# Click on Login
driver.find_element(By.XPATH, "//div[@class='left-icon bottom-left']/div[2]" ).click()
time.sleep((0.5))
# Enter Mobile Number
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("9466122122")
# Enter Password
driver.find_element(By.XPATH,"//input[@name='loginPwd']").send_keys("Shgb@8043")
# Wait time to Enter Captcha Manually
time.sleep(6)
# Login Button Click
driver.find_element(By.CSS_SELECTOR, ".genGreenBtn > span:nth-child(1)").click()
time.sleep(1)
# Popup Accept
driver.find_element(By.CSS_SELECTOR,"button.btn:nth-child(1) > span:nth-child(1)").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/aside/div[1]/ul/li[2]/a").click()
time.sleep(2)
# Select FY 2022-23
select = Select(driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div/form/div/select")).select_by_index(1)
driver.find_element(By.XPATH,'//*[@id="dashboardTabs-tab-2"]').click()
driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/div/div[1]/button").click()
# Click on Proceed button
driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/button").click()


