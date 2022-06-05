"""
Created on Aug 2021

@author: Sakshamdeep Singh
"""

from datetime import date
import urllib
import json
import time
import winsound
import win32api
#import pywhatkit

# test using bangalore urban code
# Bangalore_Urban = 265
# Jammu = 230

def getUrl():
    params = {"district_id": 230, "date": date.today().strftime("%d-%m-%Y")}
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?{}".format(urllib.parse.urlencode(params)) 
    return url

def getResponse(url):
    output = urllib.request.urlopen(url).read()
    response = json.loads(output)
    return response

# traverse sessions
def traverseSessions(sessions):
    session_slots = []
    for session in sessions:
        # filters
        # available_capacity_dose1, int 
        # min_age_limit >=18, int
        # vaccine = COVISHIELD, string
        available_capacity_dose1 = session.get("available_capacity_dose1")
        min_age_limit = session.get("min_age_limit")
        vaccine = session.get("vaccine")
        
        # for testing purpose
        '''
        if available_capacity_dose1 >= 0:
            print("available_capacity_dose1: {}".format(available_capacity_dose1))
        if min_age_limit == 18:
            print("min_age_limit: {}".format(min_age_limit))
        if vaccine == "COVISHIELD":
            print("vaccine: {}\n".format(vaccine))
        '''

        if(available_capacity_dose1 > 0 and min_age_limit == 18 and vaccine == "COVISHIELD"):
            slot = {
                "date" : session.get("date"),
                "dose 1 slots": session.get("available_capacity_dose1")
                #"dose 2 slots": session.get("available_capacity_dose2")
            }
            session_slots.append(slot)
    return session_slots
    
def alerts(message):
    #pywhatkit.sendwhatmsg('+911231231231', message, 4, 30)
    winsound.Beep(750, 5000)
    title = 'SLOT_FOUND at {}'.format(time.strftime("%H:%M:%S", time.localtime()))
    win32api.MessageBox(0, message, title, 0x00001000) 

api_calls = 0

# driver
while True:
    output_file = open("slots.txt", "a")
    api_calls +=1 
    print("\n==============================================", file=output_file) 
    print("API Call #{}\n".format(api_calls), file=output_file)
    print("API Call #{}\n".format(api_calls))

    url = getUrl()
    response = getResponse(url)

    # path: centers(array) -> center(object) -> sessions(array) -> session(object) 
    slots = []
    centers = response.get("centers")
    for center in centers:
        sessions = center.get("sessions")
        session_slots = traverseSessions(sessions)
        if len(session_slots) != 0:
            center_slots = {
                "center_name": center.get("name"),  
                "address": center.get("address"),  
                "pincode": center.get("pincode"),  
                "available_slots": session_slots
            }
            slots.append(center_slots)

    if len(slots) != 0:
        json_message = json.dumps(slots, indent=4)
        print(json_message, file=output_file)
        #alerts(json_message)
    #else:
        #print("No slot found", file=output_file)
    
    output_file.close()
    # hit api every minute
    time.sleep(60)


