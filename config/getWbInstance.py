from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from dotenv import dotenv_values
config = dotenv_values(".env")

def getWB():
    chrome_options = wd.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # wb = wd.Chrome() 
    wb = wd.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wb.implicitly_wait(10)
    wb.get(config["URL"])
    return wb