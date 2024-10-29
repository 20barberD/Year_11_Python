studentnames = ["Rob", "Anna", "Huw", "Emma", "Patrice", "lqbal"]

attendance = {}
totalPresent = 0
totalAbsent = 0
for student in studentnames:
    isPresent = input(f"Is {student} here? (Type YES or NO) ").lower()
    if isPresent == "yes":
        attendance[student] = True
        totalPresent += 1
    else:
        attendance[student] = False
        totalAbsent += 1

print(f"{totalPresent} student{'s' if totalPresent != 1 else ''} present")
print(f"{totalAbsent} student{'s' if totalAbsent != 1 else ''} absent")