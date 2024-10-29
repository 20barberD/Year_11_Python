daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

timeSpent = [
    [60, 30, 45, 0],
    [180, 60, 0, 60],
    [200, 30, 0, 20],
    [60, 10, 15, 15],
    [100, 35, 30, 45],
]

def dayOfTheWeek(number):
    for x in range(0, len(timeSpent)):
        for num in timeSpent[x]:
            if number == num:
                return daysOfTheWeek[x]
    return False

print(dayOfTheWeek(100))