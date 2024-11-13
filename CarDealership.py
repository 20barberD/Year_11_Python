def canSell(miles, age):
    return miles < 10000 and age <= 5

miles = float(input("How many miles has the car driven? "))
age = int(input("How old is the car? "))

if canSell(miles, age):
    print("We can sell this car. ")
else:
    print("We cannot sell this car. ")