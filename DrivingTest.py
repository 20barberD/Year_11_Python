def passed(minorFaults):
    return minorFaults < 16

hasPassed = passed(55)
if hasPassed:
    print("Pass!")
else:
    print("Fail!")