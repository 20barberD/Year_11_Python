def checkEmail(email):
    return '@' in email and len(email) >= 20

print(checkEmail("This is definitely not an email"))