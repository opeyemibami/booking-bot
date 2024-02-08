import time
import datetime;
  
timeOfInterest = "11:00:00"
current_time = datetime.datetime.now()
D, t = str(current_time).split(" ")
today = D[-2:]
tomorrow = D.replace(today,"0"+str(int(today)+1))
print(tomorrow)
tomorrow = map(int,tomorrow.split("-"))
yr,mnth,day = tomorrow
hr,mins,secs = map(int,timeOfInterest.split(":"))

dt = datetime.datetime(yr,mnth,day,hr,mins,secs)
print(dt.timestamp())






seconds = 1707462000

convert = time.strftime("%H:%M", time.gmtime(seconds))

print(convert)


# time_str = "21:00:00"
# def get_seconds(time_str):
#     print('Time in hh:mm:ss:', time_str)
#     # split in hh, mm, ss
#     hh, mm, ss = time_str.split(':')
#     return int(hh) * 3600 + int(mm) * 60 + int(ss)
# print('Time in Seconds:', get_seconds(time_str))

# print(time.gmtime(seconds))
# seconds = timefromdate("2013-01-26 15:36:24", "%Y-%m-%d %H:%M:%S")
# print(seconds)
1707476069