*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://www.zales.com


*** Test Cases ***
LoginTest
    create webdriver     chrome executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\chromedriver_win32\chromedriver.exe"
    Open Browser    ${url}   ${browser}
    logintoapplication
    #open browser    https://www.zales.com   chrome
    #click link  xpath:
    #input text  id:
    #click element   xpath:
    close browser


*** Keywords ***
logintoapplication
    click link  xpath:
    input text  id:
    click element   xpath:
