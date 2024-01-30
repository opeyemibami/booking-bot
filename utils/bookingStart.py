from datetime import datetime
time_now = datetime.now()
current_time = time_now.strftime("%H:%M:%S")
minute = int(current_time.split(':')[1])


booking_minute = 55
# print(minute<booking_minute)

while (minute<booking_minute):
    print(minute)
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M:%S")
    minute = int(current_time.split(':')[1])        
    
print("looking for court")
