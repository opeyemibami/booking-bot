from selenium.webdriver.common.by import By


def selectBookingDate(wb):
    dateButtons = wb.find_elements(By.CLASS_NAME,value="date_button")
    tomorrow = dateButtons[1]
    tomorrow.click()
    return