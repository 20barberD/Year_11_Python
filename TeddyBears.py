def wages(teddyBearsMade, hoursWorked):
    teddyMoney = 2 * teddyBearsMade
    hoursMoney = 5 * hoursWorked
    if teddyMoney > hoursMoney:
        return teddyMoney
    else:
        return hoursMoney

teddyBearsMade = int(input("How many teddy bears have you made? "))
hoursWorked = int(input("How many hours have you worked? "))
print(f"Your wages are £{wages(teddyBearsMade, hoursWorked)}!")