from selenium import webdriver


driver = webdriver.Firefox(executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\geckodriver-v0.30.0-win64\geckodriver.exe")
driver.get("https://web.whatsapp.com/")