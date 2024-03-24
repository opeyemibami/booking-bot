from config.getWbInstance import getWB
import time
from handler.handlers import bookCourtHandler
import os
from dotenv import dotenv_values,find_dotenv,load_dotenv
env_file = find_dotenv()
load_dotenv()
config = dotenv_values(env_file)

wb = getWB()

# TODO keep log of users

if __name__ =="__main__":
    # local session details
    bot_response = bookCourtHandler(wb,
        userId=os.environ["USERID"],
        passwd=os.environ["PASSWORD"], 
        opponent_firstName=os.environ["OPPONENT_FIRSTNAME"],
        opponent_lastName=os.environ["OPPONENT_LASTNAME"],
        book_for_tomorrow=True,
        time_of_interest="21:00",
        booking_hour ="21"
    )

    if not bot_response:
        print("no court available")

    while(bot_response):
        pass
        # time.sleep(10)
        # wb.quit()
        # break