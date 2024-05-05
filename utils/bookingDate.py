from selenium.webdriver.common.by import By

def selectBookingDate(wb,is_tomorrow):
    dateButtons = wb.find_elements(By.CLASS_NAME,value="date_button")
    if(is_tomorrow=="True"):
        tomorrow = dateButtons[1]
        tomorrow.click()
        return True
    # Book now instead
    return False