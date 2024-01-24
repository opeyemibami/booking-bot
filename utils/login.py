from selenium import webdriver as wd
from chromedriver_py import binary_path
import pandas as pd

def login(wb,userId,passwd):
    wb.find_element(value="login-btn").click()
    username = wb.find_element(value="userId")
    password = wb.find_element(value="passwd")
    username.send_keys(userId)
    password.send_keys(passwd)

    sign_button_login= wb.find_element(value="sign_in")
    sign_button_login.click()
    return 


