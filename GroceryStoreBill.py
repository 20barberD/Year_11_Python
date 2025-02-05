def formatAsMoney(number):
    text = ""
    split = str(round(number, 2)).split('.')
    text += f"{split[0]}.{split[1]}"
    if len(split[1]) < 2:
        for i in range(len(split[1]), 0, -1):
            text += "0"
    return text

def fruit_cost(weight):
    return weight * 3.50
def vegetable_cost(weight):
    return weight * 2.80
def dairy_cost(quantity):
    return quantity * 1.20
def snack_cost(quantity):
    return quantity * 2.50

fruitWeight = float(input("What is the weight of the fruits you have bought (in kg)? "))
vegetableWeight = float(input("What is the weight of the vegetables you have bought (in kg)? "))
dairyQuantity = int(input("How many dairy products have you bought? "))
snackQuantity = int(input("How many snacks have you bought? "))

totalCost = fruit_cost(fruitWeight) + vegetable_cost(vegetableWeight) + dairy_cost(dairyQuantity) + snack_cost(snackQuantity)
if totalCost > 20:
    totalCost *= 0.95
print(f"You have to pay £{formatAsMoney(totalCost)}. ")