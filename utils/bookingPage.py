from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


timeOfInterest  = "09:00"
def availableSession(wb):
    availableSess = wb.find_elements(By.CLASS_NAME,value="session")
    # print(availableSess[0].text)
    # print(len(availableSess))
    # for ses in availableSession:
    sessionOfInterest = [ses for ses in availableSess if timeOfInterest in ses.text]
    # print(sessionOfInterest.text)
    # sessionOfInterest[0].click()
    # print(dir(sessionOfInterest.get_property("onmousedown")))


 
    for sess in sessionOfInterest:
        print(dir(sess))
        # print(dir(sess.get_property("onmousedown")))
        # print(sess.get_attribute("outerHTML"))

        break
    #     wb.switch_to.new_window('tab')
    #     sess.click()
    # print(len(sessionOfInterest))
    return

# https://ebookingonline.net/box/session.php?court_id=1&court_name=Court%201&time=1706598000&start=1706594400
# https://ebookingonline.net/box/session.php?court_id=3&court_name=Court%203&time=1706598000&start=1706594400