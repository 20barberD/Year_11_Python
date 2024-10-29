gradesFile = "Grades.txt"

enteringGrades = True
with open(gradesFile, 'a') as grades:
    while enteringGrades:
        name = input("Enter the student's name: ")
        marks = int(input("How many marks did they get: "))
        grades.write(f"{name}::{marks}\n")
        wantToStop = input("Press Enter to keep entering students or type something to stop: ")
        if wantToStop != "":
            enteringGrades = False
print("\n")

topMark = 0
topStudent = False
with open(gradesFile, 'r') as grades:
    for line in grades.readlines():
        line = line.replace("\n", "")
        line = line.split("::")
        
        name = line[0]
        mark = int(line[1])
        
        if mark > topMark:
            topMark = mark
            topStudent = name

        if mark > 75:
            print(f"{name} has gotten over 75 marks! ")

if topStudent:
    print(f"{topStudent} achieved the highest mark with {topMark} mark{'s' if topMark != 1 else ''}! ")