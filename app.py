from selenium import webdriver as wd
from chromedriver_py import binary_path
import pandas as pd
from utils.login import login
from utils.bookingDate import selectBookingDate
from utils.bookingPage import availableSession

from dotenv import dotenv_values
config = dotenv_values(".env")



wb = wd.Chrome() 
wb.implicitly_wait(10)
wb.get(config["URL"])

login(wb,userId=config["USERID"],passwd=config["PASSWORD"])
# selectBookingDate(wb)
availableSession(wb)

# TODO get ready to book at a specific time
# TODO check time and availability  
# TODO open new page to see remaining courts and tabs for each available time of interest

while(True):
    pass

# if"__name__"=="__main__":
