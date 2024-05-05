from utils.login import login
from utils.bookingDate import selectBookingDate
from utils.bookingPage import getAvailableCourtsLinks, clickNextCourts, openTabs, fillPlayerName, makeBookings
from utils.bookingStart import isTimeToBookByHour


def bookCourtHandler(wb,
                    userId: int,
                    passwd, 
                    opponent_firstName: str,
                    opponent_lastName: str,
                    is_the_system_time_correct:True,
                    book_for_tomorrow=True,
                    time_of_interest="09:00",
                    booking_hour ="09"
              ):
    
    availableCourtsLinks = []
    tab_window_handles = []

    loginSuccessfuly = login(wb,userId=userId,passwd=passwd)
    # print(loginSuccessfuly)
    if not loginSuccessfuly:
        wb.quit()
        return "badCredentials"
    
    bookforTomorrow = selectBookingDate(wb,is_tomorrow=book_for_tomorrow.capitalize())
    # court 1-4
    availableCourtsLinks.extend(getAvailableCourtsLinks(wb,time_of_interest))
    # court 5-8
    clickNextCourts(wb)
    availableCourtsLinks.extend(getAvailableCourtsLinks(wb,time_of_interest))

    #open each court link on a new tap
    if(len(availableCourtsLinks)>0):
        tab_window_handles = openTabs(availableCourtsLinks,wb)
        # Fill in second player name across tabs
        fill_response = fillPlayerName(wb,tab_window_handles,opponent_firstName, opponent_lastName)
        if not fill_response:
            return "FalseOpponet"
    else:
        # No court available 
        return False
    
    if(bookforTomorrow):
        is_booking_time = isTimeToBookByHour(booking_hour=booking_hour,is_the_system_time_correct=is_the_system_time_correct)
        if(is_booking_time):
            print("making booking for tomorrow now.......")
            makeBookings(wb,tab_window_handles)
            return True
        else:
            return "tooEarly"
        
    # book today now 
    else:
        print("booking court for today now..........")
        makeBookings(wb,tab_window_handles)
        return True
