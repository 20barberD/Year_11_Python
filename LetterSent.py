studentData = [
    ["Kirstie", "Homework forgotten", -2, False],
    ["Byron", "Good effort in class", 1, True],
    ["Grahame", "100% in a test", 2, False],
    ["Marian", "Bullying", -3, True],
]

def indexOfStudentName(name):
    i = 0
    for student in studentData:
        if student[0].lower() == name.lower():
            return i
        i += 1
    return False

def letterSent(studentName):
    studentIndex = indexOfStudentName(studentName)
    return studentData[studentIndex][3]

print(letterSent(input("Enter a student name to check: ")))