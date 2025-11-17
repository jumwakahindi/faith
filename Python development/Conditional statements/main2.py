#program to disolay the current date and time
import datetime
#displaying the current time
now=datetime.datetime.now()
print("current date and time is:",now)
#format the date and time
print("formated date:", now.strftime("%H:%M %d-%m-%Y"))