import calendar
import datetime
import random
import time

# get the whole calendar
# 1.
print(calendar.calendar(2026))
# 2.
d = datetime.datetime.now()
y = d.strftime("%Y")
print(calendar.calendar(int(y)))
# 3. 
print(calendar.calendar(int(datetime.datetime.now().strftime('%Y'))))

# load the calendar of particular month
print(calendar.month(2020, 3))


# from datetime import date, time, datetime

# calling the today
# function of date class
# today = date.today()
# now = datetime.now()
# print("Today's date is ", today)
# print("\nCurrent Date and Time is ", now)

# Printing date's components
# print("\nDate components", today.year, today.month, today.day)

def getRandomDate(startDate, endDate ):  # defining function
    print("Printing random date between", startDate, " and ", endDate)
    randomGenerator = random.random()
    dateFormat = "%m/%d/%Y"

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
print("Random Date = ", getRandomDate("1/1/2016", "12/12/2018"))