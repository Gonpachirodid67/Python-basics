import datetime

# create a new date 
d = datetime.date(2026, 1, 1)
print(d.isoformat())
print(d.weekday())

# current date and time of the server
print(datetime.datetime.now())

current_time = datetime.datetime.now()

# current weekday in full form
print(current_time.strftime("%A"))
# current weekday in short
print(current_time.strftime("%a"))
# date (1 - 31)
print(current_time.strftime("%d"))
# month - full form
print(current_time.strftime("%B"))
# month - short form
print(current_time.strftime("%b"))
# year - full from
print(current_time.strftime("%Y"))
# year - short form
print(current_time.strftime("%y"))
# hours - 24 hours format
print(current_time.strftime("%H"))
# hours - 12 hours format
print(current_time.strftime("%I"))
# AM/PM
print(current_time.strftime("%p"))
# minutes
print(current_time.strftime("%M"))
# seconds 
print(current_time.strftime("%S"))
# local version of date
print(current_time.strftime("%x"))
# local version of time
print(current_time.strftime("%X"))
# local version of date and time
print(current_time.strftime("%c"))