from fastapi import FastAPI,status, Response
from handler.handlers import bookCourtHandler
from config.getWbInstance import getWB
from utils.timeUtils import getSystemTime
from validators.validator import validateBookingHour, validateApikey
import time
import uvicorn

app = FastAPI()



@app.get("/")
def api_home():
    return {"message":"bot is functional and ready to fly 😉"}


@app.get("/getSystemTime")
def api_get_system_time():
    t = getSystemTime()
    print(t)
    return {"message":f"the system time is {t}"}

@app.post("/book-a-court",status_code=200)
def bookCourt(response: Response,
              api_key:str,
              userId: int,
              passwd, 
              opponent_firstName: str,
              opponent_lastName: str,
              is_the_system_time_correct=True,
              booking_for_tomorrow=True,
              time_of_interest="09:00",
              booking_hour ="09"
              ):
    """
    For effective usage, only send request 3 mins before rush hour or booking hour!
    """

    if(not validateApikey(api_key)):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message":"Wrong Api key, try again"}
    # else:
    #     return {"message":"Good Api key"}

    t = int(time_of_interest.split(":")[0])
    if not validateBookingHour(booking_hour,t):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message":"Booking hour and time_of_interest cannot be greater than 23"}
    
    wb = getWB()
    bot_response = bookCourtHandler(wb,
        userId=userId,
        passwd=passwd, 
        opponent_firstName=opponent_firstName,
        opponent_lastName=opponent_lastName,
        is_the_system_time_correct = is_the_system_time_correct.capitalize(),
        book_for_tomorrow=booking_for_tomorrow.capitalize(),
        time_of_interest=time_of_interest,
        booking_hour =booking_hour)
    if bot_response==True:
        while(bot_response):
            time.sleep(5)
            wb.quit()
            return {"message":"Check your email to see booked court if lucky."}
    elif bot_response=="badCredentials":
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message":"Bad Credentials, please check your login details"}
    elif bot_response=="FalseOpponet":
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message":"Opponent does not exist, please confirm opponent name spelling"}
    elif(bot_response=="tooEarly"):
        return {"message: Too early, resend request about 3 minute to rush hour"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message":"So sorry, no court available for your selection"}
# TODO keep log of users

# uncomment this for local testing without using docker
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,reload=True,timeout_keep_alive=10)
