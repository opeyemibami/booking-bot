from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


timeOfInterest  = "21:00"
def getAvailableCourtsLink(wb):
    # TODO check time and availability  
    # TODO open new page to see remaining courts and tabs for each available time of interest
    availableCourts = []
    courts =  wb.find_elements(By.CLASS_NAME,value="court")
    # TODO check if time of interes in on the page, else click later time
    for court in courts:
        availableSess = court.find_elements(By.CLASS_NAME,value="session")
        sessionOfInterest = [ses for ses in availableSess if timeOfInterest in ses.text]
        if(len(sessionOfInterest)>0):
            availableCourts.append(court.find_element(By.CLASS_NAME,value="court_head").text.split(" ")[1])

    print(availableCourts)

    return

# https://ebookingonline.net/box/session.php?court_id=2&court_name=Court%202&time=1707426000&start=1707426000