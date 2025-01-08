import math

def daysInMonth(month, year):
    daysInEachMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    daysInMonth = daysInEachMonth[month-1]
    if month == 2 and year % 4 == 0:
        daysInMonth = 29
    return daysInMonth

def isValidDay(day, month, year):
    days = daysInMonth(month, year)
    return (month <= 12) and (day <= days) and (type(year) == int)

def getDayOfTheWeek(day, month, year):
    daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    daysSinceFirstJanuary = ((year - 2024) * 365) + ((year - 2024) * 1) #Years
    monthsSinceFirstJanuary = month - 1 #Find months since January
    for x in range(1, monthsSinceFirstJanuary+1): #Months
        print(x, daysInMonth(x, year-(math.floor((month-x)/12))))
        daysSinceFirstJanuary += daysInMonth(x, year-(math.floor((month-x)/12)))
    print(daysSinceFirstJanuary)
    daysSinceFirstJanuary += day-1 #Days
    print(daysSinceFirstJanuary)
    dayOfTheWeek = daysOfTheWeek[daysSinceFirstJanuary%7] #Find day of the week
    return dayOfTheWeek
    
print(getDayOfTheWeek(18, 10, 2025))