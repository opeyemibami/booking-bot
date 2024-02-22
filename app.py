from selenium import webdriver as wd
from chromedriver_py import binary_path
import pandas as pd
from utils.login import login
from utils.bookingDate import selectBookingDate
from utils.bookingPage import getAvailableCourtsLinks

from dotenv import dotenv_values
config = dotenv_values(".env")



wb = wd.Chrome() 
wb.implicitly_wait(10)
wb.get(config["URL"])
availableCourtsLinks = []

login(wb,userId=config["USERID"],passwd=config["PASSWORD"])
selectBookingDate(wb)
# court 1-4
availableCourtsLinks.extend(getAvailableCourtsLinks(wb))
# TODO Click next court button to see remaining courts and getAvailableCourtsLinks
# court 5-8
# TODO: 


# TODO get ready to book at a specific time

while(True):
    pass

# if"__name__"=="__main__":
