timeSpent = [
    [60, 30, 45, 0],
    [180, 60, 0, 60],
    [200, 30, 0, 20],
    [60, 10, 15, 15],
    [100, 35, 30, 45],
]

i = 0
for day in timeSpent:
    totalTime = 0
    for time in day:
        totalTime += time
    averageForDay = totalTime / len(day)
    print(f"{averageForDay} minutes of computer games played on average on Day {i} ")
    i += 1