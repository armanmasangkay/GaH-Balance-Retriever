from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions, Chrome
import os
import json
import time

mypath = os.path.dirname(os.path.abspath(__file__))
mypath=mypath+'/account.json'




def login():
    if (not accountFileExists()):
        createFile()

    account=getAccountValues()
    usernameStr=account['username']
    passwordStr=account['password']

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


def getAccountValues():
    with open(mypath,'r') as f:
        data=json.load(f)
    return data

def accountFileExists():
    if os.path.isfile(mypath):
        return True
    else:
        return False


def createFile():
    if (not accountFileExists):
        print('Seems like you have not set up an account yet.')
    else:
        print ('Enter new account details below')
    user=input('Enter a username:')
    pwd=input('Enter a password:')
    data={
        'username':user,
        'password':pwd
    }
    with open(mypath,'w') as f:
        json.dump(data,f)
    



