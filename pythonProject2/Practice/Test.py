import pyautogui
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait, expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
import time
import openpyxl



# import zoom as zoom
# driver = webdriver.Chrome(
    # executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\chromedriver_win32\chromedriver.exe")
driver = webdriver.Firefox(executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\geckodriver-v0.30.0-win64\geckodriver.exe")
# driver.get("http://demo.guru99.com/V4/")
# driver.get("https://web.whatsapp.com/")
# driver.get("http://demo.guru99.com/test/newtours/")
driver.get("https://www.zales.com")
driver.maximize_window()
time.sleep(8)
'''
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)
driver.get("https://www.google.com")
'''
chromeOptions = Options()
#chromeOptions.add_experimental_option("pref","")
# driver.switch_to.alert.accept()
# driver.implicitly_wait(4)
# wait= WebDriverWait(driver,10)
time.sleep(2)
# driver.find_element_by_css_selector("a.shopping-cart-btn:nth-child(1)").click()
# email_id= driver.find_element_by_css_selector("#guestuser\.emailAddrss")
# driver.find_element_by_css_selector("#guestuser\.emailAddrss").send_keys("abc@gmail.com")
# driver.find_element_by_xpath('//*[@id="guestuser.emailAddrss"]').send_keys("abc@gmail.com")
time.sleep(2)
# print(email_id.text)
# Working method using pyautogui
pyautogui.keyDown('ctrl')
pyautogui.press('-')
pyautogui.keyUp('ctrl')
# driver.command_executor.execute(zoom,"90%")
#driver.command_executor.execute("document.body.style.zoom='0.5'",)
# driver.execute_script('document.body.style.MozTransform = "scale(0.80)";')
# driver.execute_script('document.body.style.MozTransformOrigin = "0 0";')
# driver.find_element(By.PARTIAL_LINK_TEXT,"HOME")
time.sleep(1)
driver.find_element_by_css_selector("#main-container > div.main-inner > header > "
                                    "div.top-navigation.hidden-xs.hidden-sm > div > "
                                    "div.col-md-8.my-account-navigation.hidden-sm.hidden-xs.pull-right > ul > "
                                    "li.top-nav-link.sign-in > a.sidebar-login").click()
# driver.find_element_by_xpath("/html/body/main/div/div[2]/div[3]/div[6]/div[1]/nav/ul/li/div/div[1]/div[1]/ul/li[1]/a").click()
time.sleep(3)
# driver.find_element_by_xpath('//*[@id="sign-in"]').click()
driver.find_element_by_xpath('//*[@id="create-account"]').click()
# driver.execute_script("window.scrollBy(0,800)","")
# crtaccountlink= driver.find_element_by_xpath('//*[@id="signetRegisterForm"]/div[2]/div/button')
crtaccountlink2 = driver.find_element_by_css_selector("#signetRegisterForm > div.form-actions.clearfix > div > button")
# driver.execute_script("arguments[0].scrollIntoView;",crtaccountlink2)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# w= WebDriverWait(driver,2)
# w.until(expected_conditions.presence_of_element_located(By.XPATH,'//*[@id="signetRegisterForm"]/div[2]/div/button'))
time.sleep(2)
# crtaccountlink.click()
crtaccountlink2.click()
# driver.find_element_by_xpath('//*[@id="signetRegisterForm"]/div[2]/div/button').click()
driver.find_element_by_css_selector("#signetRegisterForm > div.form-actions.clearfix > div > button").click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,-900)", "")
time.sleep(2)
watches = driver.find_element_by_css_selector(
    "#stickyNav > div > nav > ul > li:nth-child(6) > div.desktop-nav-link > span > a")
watches1 = driver.find_element_by_xpath('//*[@id="stickyNav"]/div/nav/ul/li[6]/div[1]/span/a')
rose = driver.find_element_by_css_selector(
    "#stickyNav > div > nav > ul > li:nth-child(6) > div.sub-menu > div:nth-child(1) > div:nth-child(2) > ul > div:nth-child(4) > div.link-label > li > a")
rose1 = driver.find_element_by_xpath('//*[@id="stickyNav"]/div/nav/ul/li[6]/div[2]/div[1]/div[2]/ul/div[4]/div[2]/li/a')
pearl = driver.find_element_by_xpath('//*[@id="stickyNav"]/div/nav/ul/li[7]/div[2]/div[1]/div[2]/div/div[1]/ul/div['
                                     '7]/div[2]/li/a')
action = ActionChains(driver)
action.send_keys(Keys.ENTER)
action.move_to_element(watches1).click(watches1).perform()
# action.move_to_element(watches).move_to_element(rose).click().perform()
# action.move_to_element(watches1).move_to_element(rose1).click().perform()
action.move_to_element(pearl).click(pearl).perform()
# driver.find_element_by_xpath('/html/body/main/div/div[2]/div[4]/div/button').click()
# scrl2top= driver.find_element_by_xpath('//*[@id="backToTopMobile"]/div/button')
# scrl2top.click()
# driver.set_window_size(1400,900)
# driver.execute_script("document.body.style_zoom='70%'")
# gst= Select(driver.find_element_by_xpath('//*[@id="sortOptions1"]')) # For dropdown
# gst.select_by_visible_text("")# Select drop down index
# gst.select_by_value("avgRating_double_Descending")# Select by value
# gst.select_by_index(2)
#upload a file
'''driver.find_element_by_xpath('//*[@id="gbapi-global-search-form"]/div/div[1]/span[1]').click()
time.sleep(5)
driver.find_element_by_xpath(
    '//*[@id="stickyHeader"]/div/div[3]/div/div/div[1]/div[4]/div/div[2]/div[1]/label[2]/span').send_keys(
    "C:\\Users\\Kunal Talwar\\Desktop\\ticket.pdf")'''
# Open blank new tab
driver.execute_script('''window.open("", "_blank");''')
driver.execute_script('''window.open();''')

'''gst= Select(driver.find_element_by_css_selector("a.shopping-cart-btn:nth-child(1)")) # For dropdown
gst.select_by_visible_text("dropdown index values")# Select drop down index
gst.select_by_value()# Select by value
optns=gst.options
len(optns)# lenth of dropdown options
for option in optns:
    print(option.text)'''

'''email_id= driver.find_elements_by_id("guestuser.emailAddrss")
email_id.click().send_keys("abc@gmail.com")
print(email_id.is_enabled())
driver.find_element_by_css_selector("div.btn-collection:nth-child(6) > a:nth-child(1)").click()
driver.implicitly_wait(4)'''
# print(len(email_id))
# wait.untill(EC.element_to_be_clickable(By.CSS_SELECTOR,"a.shopping-cart-btn:nth-child(1)")).click()
# driver.find_element(By.data-di-id,"di-id-786a6013-b6d6bdd9").click()
# .find_elements_by_class_name("shopping-cart-btn").find_element("href=/guest/guest-order-status").click()
# abc = driver.find_element_by_css_selector("img [src=/_ui/v0000/responsive/common/images/truck.svg]")
# print(abc.is_selected())
# driver.switch_to.alert.accept()
# driver.find_element_by_class_name()
# driver.find_elements_by_class_name("shopping-cart-btn").click()
# ActionChains(driver).send_keys(Keys.CONTROL,)
'''driver.execute_script("document.body.style.zoom = ' 90% '")
driver.execute_script("document.body.style_zoom=' 90% '")

ActionChains(driver).send_keys(Keys.CONTROL,'-')
anyelement.send_keys(Keys.CONTROL,'-')# wont work probably
ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('-').key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()
driver.set_window_size(900,900,'')'''
# driver.close()
'''
driver.execute_script('document.body.style.MozTransform = "scale(0.9)";')
driver.execute_script('document.body.style.MozTransformOrigin = "0.0";')'''
'''print(driver.title)
print(driver.current_url)
print(driver.find_element_by_name('uid').is_displayed())
driver.find_element_by_name('uid').send_keys('mngr364483')
print(driver.find_element_by_name('btnLogin').is_enabled())
driver.find_element_by_name('password').send_keys('ejereja')
print(driver.find_element_by_name('btnLogin').is_enabled())
driver.find_element_by_name('btnLogin').click()
print(driver.current_url)
time.sleep(2)
driver.back()
print(driver.current_url)
driver.forward()
time.sleep(2)
print(driver.current_url)'''

'''
@click.option('--zoom', default=70, help='Zoom level')
def capture(zoom):
    driver.get("https://www.zales.com/")
    time.sleep(6)
    if zoom != 100:
        driver.execute_script(f"document.body.style.zoom='{zoom}%'")


if __name__ == '__main__':
    capture(70)

'''

'''
self.name where name is variable in function of class indicates that name is a variable of that class
super().variable/function to call variable function of inherited class, when inherited class and other class has same variable, function
_variablename to hide the variable from being inherited, and to call that, created a function within the same class which calls the function
class XYZ:
    _company = "xyz"

    def company(self):
        print("Comapny is :"+self._company)
class ABC(XYZ):
    xyz = XYZ()
    print(xyz.company) # This won't print when XYZ and ABC are two different classes in separate files
    xyz.company() # Instead this would be used


def logdata(func):
    def inner_func(x):
        print("**********************************")
        print("Starting of a function:", func.__name__)
        a = func(x)
        print(a)
        print("Ending of a function:", func.__name__)
        print("**********************************")
    return inner_func()

@logdata
def sumofNumbers(a):
    a+5

sumofNumbers(10)
'''

from appium import webdriver
import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

# Step 1 : Create "Desired Capabilities"
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel3XL'
desired_caps['app'] = '/Users/sujithreddy/Documents/Skill2Lead/Appium_Demo_App/Android/Android_Appium_Demo.apk'
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=options, direct_connection=True)

# Step 3 : "Click on the App"
ele_id = driver.find_element(AppiumBy.ID, "com.skill2lead.appiumdemo:id/EnterValue")
ele_id.click()

# Step 4 : Wait for 2 seconds
time.sleep(2)

# Step 5 : Close the driver object
driver.quit()