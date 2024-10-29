codesFile = "bookcodes.txt"

def libraryCode(title, year):
    titleSub = title[:3].upper()
    yearSub = str(year)[-1::-2]
    return titleSub + yearSub

title = input("Enter the book title: ")
year = int(input("Enter the year the book was published: "))
bookCode = libraryCode(title, year)
print(f"The book code is {bookCode}. ")

with open(codesFile, 'a') as codes:
    codes.write(f"{title}::{bookCode}\n")