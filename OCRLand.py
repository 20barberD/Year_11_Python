def canRide(height, ridingWithAdult):
    return height >= 140 or (height >= 120 and ridingWithAdult)

peopleOnRide = 0
while 8 > peopleOnRide:
    height = float(input("Enter your height in centimetres: "))
    ridingWithAdult = False
    if (140 > height and height >= 120):
        adultInput = input("Are you riding with an adult? (Type Yes or No) ").lower()
        if (adultInput == "yes"):
            ridingWithAdult = True
    if (canRide(height, ridingWithAdult)):
        print("You can ride!\n ")
        peopleOnRide += 1
    else:
        print("We can't allow you to ride!\n ")

print("8 people are on the ride! Ride starting soon! ")