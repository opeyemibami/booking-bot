from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from utils.timeUtils import getTimeInSecs
import time

def _clickLaterTime(timeOfInterest,courts,wb):
    newCourts =  courts
    lastCourtOnPageTime = newCourts[-1].find_elements(By.CLASS_NAME,value="time")[-1].text
    # print(lastCourtOnPageTime)
    while(int(lastCourtOnPageTime[:2])<int(timeOfInterest[:2])):
        wb.find_elements(By.CLASS_NAME,value="buttonw")[5].click()
        newCourts =  wb.find_elements(By.CLASS_NAME,value="court")
        lastCourtOnPageTime = newCourts[-1].find_elements(By.CLASS_NAME,value="time")[-1].text
        # print(lastCourtOnPageTime)
    return wb,newCourts


def getAvailableCourtsLinks(wb,timeOfInterest = "09:00"):
    timeOfInterestInSecs  = getTimeInSecs(timeOfInterest + ":00")
    availableCourts = []
    courts =  wb.find_elements(By.CLASS_NAME,value="court")
    wb,courts = _clickLaterTime(timeOfInterest,courts,wb)

    sessionOfInterest = []
    for court in courts:
        availableSess = court.find_elements(By.CLASS_NAME,value="session")
        sessionOfInterest = [ses for ses in availableSess if timeOfInterest in ses.text]
        
        if(len(sessionOfInterest)>0):
            courtNumber = court.find_element(By.CLASS_NAME,value="court_head").text.split(" ")[1]
            # print(courtNumber)
            courtLink = "https://ebookingonline.net/box/session.php?court_id="+courtNumber+"&court_name=Court%20"+courtNumber+"&time="+timeOfInterestInSecs+"&start="+timeOfInterestInSecs
            availableCourts.append(courtLink)

    return availableCourts

def clickNextCourts(wb):
    wb.find_elements(By.CLASS_NAME,value="buttonw")[0].click()
    return

def openTabs(links,wb):
    wb.get(links[0])

    if(len(links)>1):
        for link in links[1:]:
            wb.execute_script('window.open("{}", "_blank");'.format(link))
    return  wb.window_handles

def fillPlayerName(wb,tab_window_handles,firstName, lastName):
    current_window = wb.current_window_handle
    wb.find_element(By.NAME,value="player2").send_keys(firstName +" "+lastName)
    wb.find_element(By.ID,value="search").click()
    for tab in tab_window_handles:
        if(current_window!=tab):
            wb.switch_to.window(tab)
            wb.find_element(By.NAME,value="player2").send_keys(firstName +" "+lastName)
            wb.find_element(By.ID,value="search").click()
    return 

def makeBookings(wb,tab_window_handles):
    current_window = wb.current_window_handle
    wb.find_element(By.CLASS_NAME,value="buttong").click()
    # TODO handle timeout problem
    for tab in tab_window_handles:
        if(current_window!=tab):
            wb.switch_to.window(tab)
            # print("switch to tab: ",tab)
            # time.sleep(2)
            wb.find_element(By.CLASS_NAME,value="buttong").click()
    return