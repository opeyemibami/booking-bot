from dotenv import dotenv_values
config = dotenv_values(".env")

def validateBookingHour(booking_hour,t):
    return int(booking_hour)<24 and t<24 

def validateApikey(api_key):
    allow = config["ALLOW_USERS"].split("_")
    if api_key not in allow:
        return False
    return True