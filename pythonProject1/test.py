import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\chromedriver_win32\chromedriver.exe")
action = ActionChains(driver)
driver.get("https://demo-chatbot2go.enterprisebot.co/signin")
driver.maximize_window()

email_id = 'suraj+tester@enterprisebot.org'
password = 'E13_Tester'
login_email_element = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
next_button = driver.find_element(By.CSS_SELECTOR, 'button[name = "Next"]')


def login_email(email):
    login_email_element.send_keys(email)
    next_button.click()
    time.sleep(2)


login_email(email_id)

# -------------------------------------------------------------------------------------------


login_password_element = driver.find_element(By.CSS_SELECTOR, "input[label = 'Password']")
login_button = driver.find_element(By.CSS_SELECTOR, 'button[name = "Log In"]')


def login_password(password):
    login_password_element.send_keys(password)
    login_button.click()
    time.sleep(1)


login_password(password)

assert driver.title == 'Chatbot2Go'

# --------------------------------------------------------------------------------------
# test case 1
time.sleep(2)
add_new_intent_button = driver.find_element(By.CSS_SELECTOR, 'button[name = "Add new"]')
save_button = driver.find_element(By.ID, "intent-save-btn")
new_intent_first_entry = driver.find_element(By.XPATH, '//div[@class="work-area intent-list-div"]/ul/li[1]/span')
delete_button = driver.find_element(By.NAME, 'Delete')


# CSS = 'div[class="work-area intent-list-div"] ul li'


def new_intent(intent):
    add_new_intent_button.click()
    intent_name = driver.find_element(By.CSS_SELECTOR, 'input[id = "intent-header-name"]')
    intent_name.clear()
    intent_name.send_keys(intent)
    save_button.click()
    driver.save_screenshot("C:\\Users\\Kunal Talwar\\Pictures\\Screenshots\\Selenium\\new_intent.png")
    # to delete the one made
    # delete_button.click()
    # delete_yes = driver.find_element(By.XPATH, '//div[@class="snackbar-buttons"]/button[1]')
    # delete_yes.click()


new_intent('Accounts')


# ---------------------------------------------------------------------------------
# test case 2


def add_trigger(trigger_value):
    add_trigger_text = driver.find_element(By.XPATH, '//*[@id="trigger-input"]')
    add_trigger_text.send_keys(trigger_value)
    time.sleep(2)
    add_trigger_text.send_keys(Keys.ENTER)
    driver.save_screenshot("C:\\Users\\Kunal Talwar\\Pictures\\Screenshots\\Selenium\\new_trigger.png")
    trigger_section_expand = driver.find_element(By.XPATH, '//*[@id="trigger-section"]/div/div[1]')
    trigger_section_expand.click()


add_trigger('I am interested in account')
# ----------------------------------------------------------------------------------


def reply_for_trigger(reply_text):
    reply_tab = driver.find_element(By.CSS_SELECTOR, 'div[data-responsetab="replytab0"]')
    reply_tab.click()
    reply_text_button = driver.find_element(By.XPATH, '//*[@class="sc-hKgILt gTLZXx"]')
    reply_text_button.click()
    reply_text_editor = driver.find_element(By.ID, 'repliesnewEditor')
    reply_text_editor.send_keys(reply_text)
    reply_text_editor.send_keys(Keys.ENTER)
    driver.save_screenshot("C:\\Users\\Kunal Talwar\\Pictures\\Screenshots\\Selenium\\reply_for_new_trigger.png")


reply_for_trigger("We offer three types of accounts. Checking, Saving and Business")


'''

'''
