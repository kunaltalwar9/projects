from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.gmail.com")
driver.quit()

