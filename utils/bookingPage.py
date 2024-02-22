from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.timeUtils import getTimeInSecs

def _clickLaterTime(timeOfInterest,courts,wb):
    newCourts =  courts
    lastCourtOnPageTime = newCourts[-1].find_elements(By.CLASS_NAME,value="time")[-1].text
    while(int(lastCourtOnPageTime[:1])<int(timeOfInterest[:1])):
        wb.find_elements(By.CLASS_NAME,value="buttonw")[5].click()
        newCourts =  wb.find_elements(By.CLASS_NAME,value="court")
        lastCourtOnPageTime = newCourts[-1].find_elements(By.CLASS_NAME,value="time")[-1].text
        # print(lastCourtOnPageTime)
    return wb,newCourts


def getAvailableCourtsLinks(wb,timeOfInterest = "21:00"):
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

            # print(dir(sessionOfInterest[0]))
            
            # break


    print(availableCourts)
    # availableCourtsLinks = "https://ebookingonline.net/box/session.php?court_id=2&court_name=Court%202&time=1707426000&start=1707426000"

    return availableCourts

def navigateToPage(timeOfInterest,wb):
    
    nextCourtButton = wb.find_element()

    return