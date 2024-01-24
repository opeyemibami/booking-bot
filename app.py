from selenium import webdriver as wd
from chromedriver_py import binary_path
import pandas as pd
from utils.login import login

from dotenv import dotenv_values
config = dotenv_values(".env")



wb = wd.Chrome() 
wb.implicitly_wait(10)
wb.get(config["URL"])


login(wb,userId=config["USERID"],passwd=config["PASSWORD"])


while(True):
    pass

# if"__name__"=="__main__":
