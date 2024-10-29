def checkPassword(password: str):
    return password[0].isupper() and len(password) >= 8

passwordInput = input("Enter a password starting with a capital letter and 8 or more characters: ")
if checkPassword(passwordInput):
    print("Your password is valid! ")
else:
    print("Your password is bad. ")