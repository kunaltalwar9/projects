from selenium import webdriver
import time

driver = webdriver.Chrome(
    executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.statrys.com/")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="nav-header-bg"]/div/div/div[4]/div[2]/a/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys("Chan")
time.sleep(3)
driver.execute_script("window.scrollBy(0,1800)","")

#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.execute_script("window.scrollBy(0,900)", "")
driver.find_element_by_xpath('/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/div/div/app-signup-page/app-auth-layout/div/div/app-create-account/div[3]/button').click()
#driver.find_element_by_css_selector("body > app-root > div > mat-sidenav-container > mat-sidenav-content > div > div > app-signup-page > app-auth-layout > div > div > app-create-account > div:nth-child(3) > button").click()
assert  driver.find_element_by_link_text("Please ")





#//*[@id="Sign_form"]/div[1]/div/div[1]/mat-form-field/div/div[1]/div
#//*[@id="mat-input-0"]