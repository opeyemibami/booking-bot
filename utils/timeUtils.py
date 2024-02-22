import datetime

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
  


# timeOfInterest = "23:00:00"
# current_datetime = datetime.datetime.now()
# D, t = str(current_datetime).split(" ")

# today = D[-2:]
# tomorrow = D.replace(today,str(int(today)+1))
# # print(tomorrow)
# tomorrow = map(int,tomorrow.split("-"))
# yr,mnth,day = tomorrow
# hr,mins,secs = map(int,timeOfInterest.split(":"))

# dt2 = datetime.datetime(yr,mnth,day,hr,mins,secs)
# timeOfInterestInSecs = int(dt2.timestamp())

# print(timeOfInterestInSecs)




# seconds = 1708603200
# convert = time.strftime("%H:%M", time.gmtime(seconds))
# print(convert)