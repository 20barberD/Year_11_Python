usernames = ["20barberD", "username", "bushman101", "otherCoolUsername"]

enteredUsername = input("Enter in a username: ")
if enteredUsername in usernames:
    print("That username is already in use! ")
else:
    print("That username is free! ")