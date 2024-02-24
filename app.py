from selenium import webdriver as wd
from chromedriver_py import binary_path
import pandas as pd
from utils.login import login
from utils.bookingDate import selectBookingDate
from utils.bookingPage import getAvailableCourtsLinks, clickNextCourts, openTabs, fillPlayerName, makeBookings
from utils.bookingStart import isTimeToBookByHour

from dotenv import dotenv_values
config = dotenv_values(".env")

# session details
firstName = "Jack"
lastName = "kennedy"
is_tomorrow = True
timeOfInterest = "14:00"
booking_hour = "09"
is_rushHour = True  #09:00


wb = wd.Chrome() 
wb.implicitly_wait(10)
wb.get(config["URL"])

availableCourtsLinks = []
tab_window_handles = []

login(wb,userId=config["USERID"],passwd=config["PASSWORD"])
selectBookingDate(wb,is_tomorrow=is_tomorrow)
# court 1-4
availableCourtsLinks.extend(getAvailableCourtsLinks(wb,timeOfInterest))
# court 5-8
clickNextCourts(wb)
availableCourtsLinks.extend(getAvailableCourtsLinks(wb,timeOfInterest))

#open each court link on a new tap
if(len(availableCourtsLinks)>0):
    tab_window_handles = openTabs(availableCourtsLinks,wb)
    # Fill in second player name across tabs
    fillPlayerName(wb,tab_window_handles,firstName, lastName)

# TODO book at a specific time
is_booking_time = isTimeToBookByHour(booking_hour=booking_hour)
makeBookings(wb,tab_window_handles)

while(True):
    pass

# if"__name__"=="__main__":