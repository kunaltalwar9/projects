from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
    #executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\geckodriver-v0.30.0-win64\geckodriver.exe")

driver.implicitly_wait(5)#Global wait throughout program till element found
action = ActionChains(driver)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
time.sleep(1)
# driver.find_element_by_id("autosuggest").send_keys("IND")
driver.find_element(By.ID,"autosuggest").send_keys("IND")
time.sleep(1)
# countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a ")
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a ")
print(len(countries))
for i in countries:
    print(i.text)
    if i.text == "India":
        i.click()
        break
# name = driver.find_element_by_id("autosuggest").get_attribute("value")
name = driver.find_element(By.ID,"autosuggest").get_attribute("value")
print(name)
assert name == "India"
#for handling javascripts pop up alerts
##alert.accept()
#alert.dismiss()

'''
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
time.sleep(1)
products = driver.find_elements_by_css_selector("div[class='products'] div h4")
print(len(products))
driver.find_element_by_css_selector("input[class='search-keyword']").send_keys("Ca")
time.sleep(1)
productsnames = driver.find_elements_by_css_selector("h4[class='product-name']")
#for k in productsnames:
#    print(k.text)
productprice = driver.find_elements_by_css_selector("div[class='product'] p")

j = 0
#for i in productprice:
#    print(i.text)
#   j = j + int(i.text)

for i in productprice:
    for k in productsnames:
        print(k.text,i.text)
    j = j + int(i.text)

addcarts = driver.find_elements_by_css_selector("div[class='product-action'] button")
# xpath/parent::tagname/parent::tagname- to reach grand parent xpath from already used xpath
cartproducts= []
for i in addcarts:
    cartproducts.append(i.find_element_by_xpath("parent::div/parent::div/h4").text)
    i.click()
cartvalue = int(driver.find_element_by_xpath("//div[@class='cart-info']/table/tbody/tr[2]/td[3]/strong").text)
    #driver.find_element_by_css_selector("div[class='cart-info'] strong")

print(j)
assert j == cartvalue
if j == cartvalue:
    print("Cart sums up correct")

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
'''
'''
try:
    driver.find_element_by_css_selector("input[class='promoCode']").send_keys("promocode")
    driver.find_element_by_css_selector(".promoBtn").click()
    if driver.find_element_by_css_selector(".promoInfo").text == "Invalid code ..!":
        print("Invalid code ..!")
    time.sleep(4)
except:
    driver.find_element_by_css_selector("input[class='promoCode']").clear()
    driver.find_element_by_css_selector("input[class='promoCode']").send_keys("rahulshettyacademy")
    driver.find_element_by_css_selector(".promoBtn").click()
    time.sleep(4)
'''
'''
wait = WebDriverWait(driver, 8)
#wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"span.promoCode")))
driver.find_element_by_css_selector("input[class='promoCode']").clear()
driver.find_element_by_css_selector("input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
#wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))
print(driver.find_element_by_css_selector(".promoInfo").text)

#print(driver.find_element_by_xpath("//table[@class='cartTable']/tbody/tr[1]/td[2]").text)
checkoutproducts = driver.find_elements_by_xpath("//p[@class='product-name']")
checkoutproductsnames= []
for i in checkoutproducts:
    checkoutproductsnames.append(i.text)


print(cartproducts)
print(checkoutproductsnames)
if checkoutproductsnames == cartproducts:
    print("Products Match in cart and checkout")
assert checkoutproductsnames == cartproducts, "Products Match in cart and checkout"

assert driver.find_element_by_css_selector("span.discountPerc").text == '10%'
if driver.find_element_by_css_selector("span.discountPerc").text == '10%':
    print("discount percent matches i.e", driver.find_element_by_css_selector("span.discountPerc").text )

assert float(driver.find_element_by_css_selector("span.discountAmt").text) == cartvalue-0.1*cartvalue
if float(driver.find_element_by_css_selector("span.discountAmt").text) == cartvalue-0.1*cartvalue:
    print("discount amount macthes i.e", cartvalue-0.1*cartvalue)

quantity = []
price = []
total = []
for i in driver.find_elements_by_css_selector("p[class='quantity']"):
    quantity.append(int(i.text))
for i in driver.find_elements_by_xpath("//table[@id='productCartTables']/tbody/tr/td[4]/p"):
        price.append(int(i.text))
for i in driver.find_elements_by_xpath("//table[@id='productCartTables']/tbody/tr/td[5]/p"):
    total.append(int(i.text))
noofitems = len(driver.find_elements_by_xpath("//table[@id='productCartTables']/tbody/tr/td[5]/p"))
print(quantity)
print(price)
print(total)
'''
'''
for i in (0,noofitems):
    print(quantity[i] * price[i])
    #print(quantity.append(i) * price.append(i))
    #if quantity[i]*price[i] == total[i]:
        #print("price matches")
'''
'''
#driver.switch_to.frame("#frameid or frame name or index value")
#driver.switch_to.default_content()

'''
'''
driver.get("https://rahulshettyacademy.com/angularpractice/")
firefox_options = webdriver.FirefoxOptions()
driver.execute_script("document.body.style.zoom='70%'")

time.sleep(1)
driver.find_element_by_name("name").send_keys("Hello")
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))# return statement to return the value
shopbutton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click;", shopbutton)# arguments[0] for the first variable shopbutton,
# n no of variables could be given with comma separation, n argumnets[n-1] could be the for index value to execute
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# from console directory name\ py.test : all files in the director, py.test -v -s : all files detailed report
# py.test testcase name : will run only testcase, py.test -k ABCD : will runtestcases whose namecontains ABCD
'''

#driver.quit()





