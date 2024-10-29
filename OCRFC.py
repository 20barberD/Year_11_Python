goals = [0, 1, 3, 0, 4, 5, 2, 0, 2, 1]

nogoalscount = 0
for count in range(0, len(goals)-1):
    if goals[count] == 0:
        nogoalscount += 1

print(nogoalscount)