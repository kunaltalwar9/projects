from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\geckodriver-v0.31.0-win64"
                                           r"\geckodriver.exe")
action = ActionChains(driver)
driver.get("https://jsapps.ceut0gop3e-theworkwe3-d1-public.model-t.cc.commerce.ondemand.com")
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("suresh.vikram@workweargroup.com.au")
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys("Admin12345")
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
time.sleep(5)
driver.execute_script("window.scrollBy(0, 700)", "")
# driver.get("https://jsapps.ceut0gop3e-theworkwe3-d1-public.model-t.cc.commerce.ondemand.com/search/CAT9XP")
driver.find_element(By.XPATH, '//input[@placeholder="Search by keyword"]').send_keys("CAT9XP")
time.sleep(1)
driver.find_element(By.XPATH, '//input[@placeholder="Search by keyword"]').send_keys(Keys.ENTER)
driver.execute_script("window.scrollBy(0, 700)", "")
time.sleep(2)
# action.send_keys(Keys.ENTER)
product_name = 'a[class="pname"]'
driver.find_element(By.CSS_SELECTOR, product_name).click()
time.sleep(6)
# driver.execute_script("window.scrollBy(0, 600)", "")
element_size_6 = '//div[@class="row no-gutters"]/app-pdp-size[1]/div[1]/div[1]'
# driver.find_element(By.XPATH, element_size_6).click()
element_size_8 = '//div[@class="row no-gutters"]/app-pdp-size[2]'
driver.find_element(By.XPATH, element_size_8).click()
# sizes = driver.find_elements(By.XPATH, '//div[@class="row no-gutters"]/app-pdp-size')
# for size in sizes:
#    print(size.text)
# sel = Select(driver.find_element(By.ID, "mat-select-value-1"))
# sel.select_by_index(1)
driver.find_element(By.ID, "mat-select-value-1").click()
time.sleep(2)
driver.find_element(By.ID, "mat-option-0").click()
driver.execute_script("window.scrollBy(0, 700)", "")
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'span[class="checkoutButton"]').click()
time.sleep(7)
driver.execute_script("window.scrollBy(0, 900)", "")
continue_btn = '//div[@class="cx-review container"]/div/div/button'
driver.find_element(By.XPATH, continue_btn).click()
time.sleep(3)
driver.execute_script("window.scrollBy(0, 600)", "")
continue_btn2 = '//p[@class="detailsInfo"]//parent::div/div[2]/button'
driver.find_element(By.XPATH, continue_btn2).click()
time.sleep(3)
driver.execute_script("window.scrollBy(0, 1600)", "")
continue_btn3 = '//div[@class="col-12 col-sm-3"]/button'
driver.find_element(By.XPATH, continue_btn3).click()
time.sleep(2)
driver.execute_script("window.scrollBy(0, -600)", "")
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

