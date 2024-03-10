from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from chromedriver_py import binary_path
import time

def login(wb,userId,passwd):
    wb.find_element(value="login-btn").click()
    username = wb.find_element(value="userId")
    password = wb.find_element(value="passwd")
    username.send_keys(userId)
    password.send_keys(passwd)

    sign_button_login= wb.find_element(value="sign_in")
    sign_button_login.click()
    
    try:
        time.sleep(3) #To allow login operation completion
        #check if error on login
        login_message = wb.find_element(By.ID,value="login_msg").text
        print(login_message)
        # if(len(login_message>0)):
        return False
    except:
        print("successfully login")
        return True

    
        
     


