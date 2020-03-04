from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions, Chrome
import time
import json

def login():
    usernameStr='user'
    passwordStr='crisjohn1111'

  
    opts=ChromeOptions()
    opts.add_experimental_option('detach',True)

    browser=Chrome(executable_path='chromedriver',chrome_options=opts)
    browser.get('http://192.168.254.254/html/overview.html')

    loginBtn=browser.find_element_by_id('logout_span')
    loginBtn.click()



    username=browser.find_element_by_id('username')
    username.send_keys(usernameStr)
    password=browser.find_element_by_id('password')
    password.send_keys(passwordStr)

    popLogin=browser.find_element_by_id('pop_login')
    popLogin.click()

    #sends a message
    send_message(browser)
    
def waitBeforeQuit(waitTime,browser):
    time.sleep(waitTime)
    browser.quit()


def send_message(browser):
    number='8080'
    message='DATA BAL'

    smsBtn=WebDriverWait(browser,10).until(
        EC.element_to_be_clickable((By.ID,'sms'))
    )
    smsBtn.click()

    msgBtn=browser.find_element_by_id('message')
    msgBtn.click()

    recep=browser.find_element_by_id('recipients_number')
    recep.send_keys(number)

    mes=browser.find_element_by_id('message_content')
    mes.send_keys(message)

    popSend=browser.find_element_by_id('pop_send')
    popSend.click()

    popOk=WebDriverWait(browser,20).until(
        EC.visibility_of_element_located((By.ID,'pop_OK'))
    )
    popOk.click()

    #waitBeforeQuit(5,browser)

def createFile():
    data={
        'username':'',
        'password':''
    }
    with open('account.json','w') as f:
        json.dump(data,f)
    



