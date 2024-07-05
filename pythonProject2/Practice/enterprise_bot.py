from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\geckodriver-v0.30.0-win64\geckodriver.exe")
action = ActionChains(driver)


login_email = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
save_button = driver.find_element(By.NAME, 'save_button')
add_new_intent_button = driver.find_element(By.NAME, 'add_new_button')
intent_entry = driver.find_element(By.NAME, 'respective entry')
new_intent_first_entry = driver.find_element(By.CSS_SELECTOR, 'first element of the list of intents')
triggers_section_expand = driver.find_element(By.ID, 'trigger_tab')
add_trigger_field = driver.find_element(By.ID, 'trigger_field')
reply_tab = driver.find_element(By.NAME, 'reply_tab')
reply_button = driver.find_element(By.NAME, 'reply_button')
add_reply_field = driver.find_element(By.ID, 'reply_field')
context_button = driver.find_element(By.NAME, 'context')
add_context_out_field = driver.find_element(By.NAME, 'context_out')
add_context_in_field = driver.find_element(By.NAME, 'context_in')


# ---------------------------------------------------------------------------------------------
# test_case_1
def new_intent(intent):
    add_new_intent_button.click()
    intent_name = driver.find_element(By.ID, 'intent_field')
    intent_name.send_keys(intent)
    save_button.click()
    driver.save_screenshot("name of folder where want to save screenshot.\\+new_intent.png")
    assert new_intent_first_entry.get_attribute('text') == intent


new_intent('Accounts')


# -----------------------------------------------------------------------------------------------------------
# test_case_2
def new_trigger(trigger):
    triggers_section_expand.click()
    add_trigger_field.send_keys(trigger)
    action.send_keys(Keys.ENTER)


new_trigger('I am interested in account')


# -----------------------------------------------------------------------------------------------------------
# test_case_3

def reply_for_trigger(reply_for_the_trigger):
    intent_entry.click()
    reply_tab.click()
    reply_button.click()
    add_reply_field.is_displayed()
    add_reply_field.send_keys(reply_for_the_trigger)
    action.send_keys(Keys.ENTER)
    driver.save_screenshot("name of folder where want to save screenshot.\\+new_reply_for_trigger.png")


reply_for_trigger('We offer three types of accounts. Checking, Saving and Business')


# ------------------------------------------------------------------------------------------------------

# test_case_5

def actions_using_context(context_out, context_in):
    new_intent('Open an account w/co Yes')
    existing_intent = driver.find_element(By.NAME, 'existing intent name')
    existing_intent.click()
    context_button.click()
    # if pop up is in different frame, need to use iframes
    add_context_out_field.send_keys(context_out)
    action.send_keys(Keys.ENTER)
    save_button.click()
    new_intent_created = driver.find_element(By.NAME, 'new intent name')
    new_intent_created.click()
    context_button.click()
    add_context_in_field.send_keys(context_in)
    action.send_keys(Keys.ENTER)
    save_button.click()


actions_using_context('openaccount', 'openaccount')



