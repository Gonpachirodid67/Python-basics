import datetime

# create a new date 
d = datetime.date(2026, 1, 1)
print(d.isoformat())
print(d.weekday())

# current date and time of the server
print(datetime.datetime.now())