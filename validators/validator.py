from dotenv import dotenv_values,find_dotenv,load_dotenv
env_file = find_dotenv()
load_dotenv(env_file)

# config = dotenv_values(".env")
config = dotenv_values(env_file)
print(config)

def validateBookingHour(booking_hour,t):
    return int(booking_hour)<24 and t<24 

def validateApikey(api_key):
    allow = config["ALLOW_USERS"].split("_")
    if api_key not in allow:
        return False
    return True