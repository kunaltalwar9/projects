from selenium import webdriver
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.google.co.in")
search_box = driver.find_element(By.CSS_SELECTOR,"textarea[id='APjFqb']")

# Send keys to the search input field to trigger search suggestions
search_box.send_keys("Walmart")
# Wait for a moment to let the suggestions appear
time.sleep(2)
# Locate the dropdown menu that displays the search suggestions
suggestions = driver.find_elements(By.CSS_SELECTOR,"div[class='wM6W7d'] span")

# Capture and print the search suggestions
print("Search suggestions:")
for suggestion in suggestions:
    print(suggestion.text)


action = ActionChains(driver)
action.send_keys(Keys.ENTER).perform()
time.sleep(2)
driver.switch_to.alert.accept()

