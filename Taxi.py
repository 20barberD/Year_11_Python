numberOfPassengers = int(input("Enter the number of passengers: "))
distance = int(input("How many miles have you travelled (as an integer)? "))

def price(passengers, distance):
    totalPrice = 0
    if distance >= 1:
        totalPrice += 3
        totalPrice += (distance-1)*2
    if passengers >= 5:
        totalPrice *= 1.5
    return totalPrice

print(f"The price is £{price(numberOfPassengers, distance)}")