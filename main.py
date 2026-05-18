import webbrowser
from datetime import datetime
from datetime import date
#imports pandas as pandas so you can call it by its name (example, i call it as curry and i call it curry. etc)
import time as time

url = input("Enter the meeting URL: ")
date = input("Enter the meeting date (YYYY-MM-DD): ")
timeOfMeeting = input("Enter the meeting time (HH:MM)")
another_meeting = input("Do you want to add another meeting?")

while (another_meeting == "yes"):
    url = input("Enter the meeting URL: ")
    date = input("Enter the meeting date (YYYY-MM-DD): ") 
    time = input("Enter the meeting time (HH:MM) in 24 hour form. eg 15:26")
    another_meeting = input("Do you want to add another meeting?")


while (1==1):
    currentTime = datetime.now().strftime("%H:%M")
    currentDate = datetime.now().strftime("%Y-%m-%d")
    if(currentDate == date):
        print("Dates same.")
        if(currentTime == timeOfMeeting):
            print("Same time. ")
            webbrowser.open_new_tab(url)
            time.sleep(60)
    time.sleep(1)