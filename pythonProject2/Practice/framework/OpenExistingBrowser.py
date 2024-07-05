import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import numpy

'''
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
chrome_driver = "C:\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)
'''
'''
firefox_options = Options()
# chrome_options = Options()
firefox_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
'''
'''

from selenium import webdriver
firefox_services = Service(executable_path=r"C:\\Users\Kunal Talwar\eclipse-workspace\libs\geckodriver-v0.30.0-win64\geckodriver.exe", port=3000, service_args=['--marionette-port', '2828', '--connect-existing'])
driver = webdriver.Firefox(service=firefox_services)
wait = WebDriverWait(driver, 20)
driver.get('https://youtube.com')

# driver = webdriver.Firefox(setattr(['--marionette-port', '2828', '--connect-existing']))

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"C:\\Users\Kunal Talwar\eclipse-workspace\libs\chrome-win64\chrome.exe"
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://youtube.com')

import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

subprocess.Popen('"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe" --remote-debugging-port=9222',
                 shell=True)

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome( options=options)
'''
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_options.add_argument('--remote-debugging-port=9222')
# Change chrome driver path accordingly
chrome_driver = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://youtube.com')
'''
'''
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


subprocess.Popen('"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222', shell=True)

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# options.add_argument('--remote-debugging-port=9222')
driver = webdriver.Chrome(options=options)
driver.get('https://youtube.com') 
'''
'''
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:8989")
driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
# driver =webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
# driver =webdriver.Chrome(service=Service(ChromeDriverManager(version="121.0.6167.85").install()),options=chrome_options)
driver.maximize_window()
driver.get('https://youtube.com')

'''

'''
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


subprocess.Popen('"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222', shell=True)

options = Options()
# options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.add_argument('--remote-debugging-port=9222')
driver = webdriver.Chrome(options=options)
driver.get('https://youtube.com')
'''
'''

driver = webdriver.Firefox(service=Service(port=8888))
driver.get('https://youtube.com')



chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "localhost:8989")
chrome_options.add_experimental_option("detach", True)
driver =webdriver.Chrome(service=Service(ChromeDriverManager(version="121.0.6167").install()),options=chrome_options)
# driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://youtube.com')


firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
firefox_options.add_argument('--disable-blink-features=AutomationControlled')
browser = webdriver.Firefox()

caps = DesiredCapabilities.FIREFOX
caps['marionette'] = True
driver = webdriver.Remote(
        command_executor='http://localhost:{port}'.format(port=2828))



firefox_options = Options()
firefox_options.add_argument("'--marionette-host', '127.0.0.1', '--connect-existing'")
driver = webdriver.Firefox(options=firefox_options)
# driver.get('https://youtube.com')
action = ActionChains(driver)
action.key_down(Keys.TAB).key_down(Keys.ALT).key_up(Keys.TAB).perform()



from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

firefox_options = Options()
firefox_options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Firefox(options=firefox_options)
driver.maximize_window()
driver.get("https://www.google.com")
'''
'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver =webdriver.Chrome(options=chrome_options)
driver.get("https:///www.google.com")
'''
'''
desired_caps = {
    'browserName':'firefox',
    'moz:firefoxOptions': {'debuggerAddress':'127.0.0.1:2828'}
}

driver = webdriver.Remote('http://localhost:2828/', desired_caps)
driver.get("https:///www.google.com")

# driver = webdriver.Remote('http://127.0.0.1:2828', desired_caps)
'''
'''
from sympy import symbols, Eq, solve

print("100 questions paper")
X1= int(input("X1 value"))
Y1 = 100-X1
eq1 = 4*X1 - Y1

print(f'{"When Total 100 questions attempted: "}{"Correct answers: "}{X1}{" Incorrect Answers: "}{Y1}{" Marks Scored :"}{eq1}')


X2= int(input("X2 value"))
Y2 = 90-X2
eq2 = 4*X2 - Y2

print(f'{"When Total 90 questions attempted: "}{"Correct answers: "}{X2}{" Incorrect Answers: "}{Y2}{", Marks Scored :"}{eq2}')



X3= int(input("X3 value"))
Y3 = 80-X3
eq3 = 4*X3 - Y3

print(f'{"When Total 80 questions attempted: "}{"Correct answers: "}{X3}{" Incorrect Answers: "}{Y3}{", Marks Scored :"}{eq3}')

X4= int(input("X4 value"))
Y4 = 70-X4
eq4 = 4*X4 - Y4

print(f'{"When Total 70 questions attempted: "}{"Correct answers: "}{X4}{" Incorrect Answers: "}{Y4}{", Marks Scored :"}{eq4}')

print("75 Questions Paper")
X5= int(input("X5 value"))
Y5 = 75-X5
eq5 = 4*X5 - Y5

print(f'{"When Total 75 questions attempted: "}{"Correct answers: "}{X5}{" Incorrect Answers: "}{Y5}{", Marks Scored :"}{eq5}')


X6= int(input("X6 value"))
Y6 = 65-X6
eq6 = 4*X6 - Y6

print(f'{"When Total 65 questions attempted: "}{"Correct answers: "}{X6}{" Incorrect Answers: "}{Y6}{" Marks Scored :"}{eq6}')


X7= int(input("X7 value"))
Y7 = 55-X7
eq7 = 4*X7 - Y7

print(f'{"When Total 55 questions attempted: "}{"Correct answers: "}{X7}{" Incorrect Answers: "}{Y7}{" Marks Scored :"}{eq7}')


# print("Values of 2 unknown variable are as follows:")

# print(solve((eq1), (X, Y)))
'''
'''
# Self Trial

from selenium import webdriver
firefox_options = Options()
firefox_services = Service(executable_path=r"C:\\Users\Kunal Talwar\eclipse-workspace\libs\geckodriver-v0.30.0-win64\geckodriver.exe", port=3000, service_args=['--marionette-port', '2828', '--connect-existing'])
firefox_options.add_argument("'--marionette-host', '127.0.0.1', '--connect-existing'")
firefox_options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Firefox(service=firefox_services, options= firefox_options)
time.sleep(2)
driver.get('https://youtube.com')
'''



