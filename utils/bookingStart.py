from datetime import datetime
import time


def isTimeToBookByHour(booking_hour,is_the_system_time_correct):
    booking_hour = int(booking_hour)
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M:%S")
    hour = int(current_time.split(':')[0]) 
    if (is_the_system_time_correct=="False"):
        # Winter is here: (Time moved backward by 1) 
        booking_hour += 1

    # Enforcing 5 mins to booking during rush hour
    system_minutes = int(time_now.strftime("%H:%M:%S").split(":")[1])
    if((60-system_minutes) <= 5):
        while (hour!=booking_hour):
            print("is not booking time yet: ",current_time)
            time_now = datetime.now()
            current_time = time_now.strftime("%H:%M:%S")
            hour = int(current_time.split(':')[0])   
        # delay for 2 secs 
        time.sleep(2)
        return True
    else:
        return False

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