password = ""
passwordValidated = False
while not passwordValidated:
    passwordInput = input("Enter a password with 8 or more characters: ")
    if len(passwordInput) >= 8:
        passwordValidated = True
        print("Password created! ")
    else:
        print("That password is too short! Try again!")