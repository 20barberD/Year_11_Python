name = input("Enter your name: ")
if name != "":
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You can go through. ")
    else:
        print("Leave! ")
else:
    print("Enter in a name! ")