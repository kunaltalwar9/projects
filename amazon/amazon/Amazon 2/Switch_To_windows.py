import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.amazon.in")
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_mobiles']").click()
driver.execute_script("window.scrollBy(0,8800)","")
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
elements = driver.find_elements(By.CSS_SELECTOR, "h2[class='a-size-mini a-spacing-none a-color-base s-line-clamp-4'] a span")
for i in elements:
    if elements.index(i) <= 5:
        i.click()
print(len(driver.window_handles))
for j in range(1,7):
    driver.switch_to.window(driver.window_handles[j])
    time.sleep(1.5)
    print(driver.find_element(By.CSS_SELECTOR, "span[id='productTitle']").text)
    if driver.find_element(By.CSS_SELECTOR, "span[id='productTitle']").text.find("iQOO") != -1:
        print("This is the product")
        break


