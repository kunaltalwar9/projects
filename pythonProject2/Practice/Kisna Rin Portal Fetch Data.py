import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import openpyxl
import pytest

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
time.sleep(9)
# Login Button Click
driver.find_element(By.CSS_SELECTOR, ".genGreenBtn > span:nth-child(1)").click()
wait = WebDriverWait(driver, 600)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"button.btn:nth-child(1) > span:nth-child(1)")))
# Popup Accept
time.sleep(3)
# driver.find_element(By.CSS_SELECTOR,"button.btn:nth-child(1) > span:nth-child(1)").click()
# Click on Dashboard
driver.find_element(By.CSS_SELECTOR, "aside.bg-light:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1) > span:nth-child(2)").click()
# Select Financial year
time.sleep(1)
select1 = Select(driver.find_element(By.CSS_SELECTOR,"select[name='financialYear']")).select_by_index(1)
time.sleep(1)
# Click on View Details under Preselected Loan Application Tab
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/div/div[1]/button").click()
time.sleep(1)
# Click on Proceed button
driver.find_element(By.CSS_SELECTOR, "button[class='btn genGreenBtn ms-3 text-uppercase']").click()
time.sleep(1)
table1 = driver.find_element(By.CSS_SELECTOR, "table[class='issCustomTable table']")
rows= table1.find_elements(By.TAG_NAME, 'tr')
for i in range(0,len(rows)): #for i in rows:
    row = rows[i]
    cells = row.find_elements(By.TAG_NAME, 'td')
    cell_values = [cell.text for cell in cells]
    # print(cell_values)
    path1 = "C:\\Users\\Kunal Talwar\\Downloads\\Rin Portal\\Test.xlsx"
    workbook = openpyxl.load_workbook(path1)
    sheet = workbook.active
    sheet.append(cell_values)
    time.sleep(1)
    for m in range(1,5):
        xpath = f'/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]/div[4]/div/div/div/div/table/tbody/tr[{m}]/td[8]/div/button'
        time.sleep(1)
        driver.find_element(By.XPATH, xpath).click()
        table2 = driver.find_element(By.CSS_SELECTOR, "table[class='viewmode-tble table']")
        nested_tables = table2.find_elements(By.TAG_NAME, 'table')
        # Iterate through each nested table
        for table in nested_tables:
            # Find all rows within the table
            rows = table.find_elements(By.TAG_NAME, "tr")

            # Iterate through each row
            for row in rows:
                # Find all cells within the row
                cells = row.find_elements(By.TAG_NAME, "td")

                # Print values from each cell
                for cell in cells:
                    row_data = [cell.text for cell in cells]
                    sheet.append(row_data)
        time.sleep(1)
        driver.back()

'''
        # Iterate over each table found within divs
        for table_index, table in enumerate(nested_tables, start=1):
            print(f"\nTable {table_index}:")

            # Find all rows <tr> inside the current table
            rows = table.find_elements(By.TAG_NAME, 'tr')

            # Iterate over each row and print its cell <td> values
            for row_index, row in enumerate(rows, start=1):
                cells = row.find_elements(By.TAG_NAME, 'td')
                cell_values = [cell.text for cell in cells]
                print(f"Row {row_index}: {cell_values}")
                time.sleep(1)
                driver.back()
'''


