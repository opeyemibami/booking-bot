import datetime
import time

def getTimeInSecs(time):
    timeOfInterest = time
    current_datetime = datetime.datetime.now()
    D, t = str(current_datetime).split(" ")

    today = D[-2:]
    tomorrow = D.replace(today,str(int(today)+1))
    # print(tomorrow)
    tomorrow = map(int,tomorrow.split("-"))
    yr,mnth,day = tomorrow
    hr,mins,secs = map(int,timeOfInterest.split(":"))

    dt2 = datetime.datetime(yr,mnth,day,hr,mins,secs)
    timeOfInterestInSecs = str(int(dt2.timestamp()))

    return timeOfInterestInSecs

def getSystemTime():
    """
    return system time in hour
    """
    time_now = datetime.datetime.now()
    current_time = time_now.strftime("%H:%M:%S")
    # current_hour = current_time.split(":")[0]
    return current_time
