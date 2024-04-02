from datetime import datetime
import time

def isTimeToBookByHour(booking_hour):
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M:%S")
    hour = int(current_time.split(':')[0]) 
    # Spring time (Time moved backward by 1) 
    booking_hour = int(booking_hour)-1

    while (hour!=booking_hour):
        print("is not booking time yet: ",current_time)
        time_now = datetime.now()
        current_time = time_now.strftime("%H:%M:%S")
        hour = int(current_time.split(':')[0])   

    # delay for 2 secs 
    time.sleep(2)
    print("click confirm booking button now...........")
    return True

def isTimeToBookByMinute(booking_minute):
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M:%S")
    minute = int(current_time.split(':')[1])  

    while (minute<int(booking_minute)):
        print("is not booking time yet: ",current_time)
        time_now = datetime.now()
        current_time = time_now.strftime("%H:%M:%S")
        minute = int(current_time.split(':')[1])   

    # delay for 2 secs 
    time.sleep(2)
    print("click confirm booking button now...........")
    return True