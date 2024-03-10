from selenium import webdriver as wd
from dotenv import dotenv_values
config = dotenv_values(".env")

def getWB():
    wb = wd.Chrome() 
    wb.implicitly_wait(10)
    wb.get(config["URL"])
    return wb