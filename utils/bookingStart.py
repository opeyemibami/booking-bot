from datetime import datetime
import time

def isTimeToBookByHour(booking_hour):
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M:%S")
    hour = int(current_time.split(':')[0])  

    while (hour!=int(booking_hour)):
        print("is not booking time yet: ",current_time)
        time_now = datetime.now()
        current_time = time_now.strftime("%H:%M:%S")
        hour = int(current_time.split(':')[0])   

    # TODO delay for 2 secs 
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

    # TODO delay for 2 secs 
    time.sleep(2)
    print("click confirm booking button now...........")

    return True

# isTimeToBookByMinute("16")
# isTimeToBookByHour("09")

# time_now = datetime.now()
# current_time = time_now.strftime("%H:%M:%S")
# print(current_time)
# minute = int(current_time.split(':')[1])



# booking_minute = 45
# # print(minute<booking_minute)

# while (minute<booking_minute):
#     print(minute)
#     time_now = datetime.now()
#     current_time = time_now.strftime("%H:%M:%S")
#     minute = int(current_time.split(':')[1])        
    
# print("looking for court")