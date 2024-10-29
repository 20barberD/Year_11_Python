def depreciate(value, depreciationRate, minResale):
    depreciatedValue = value * depreciationRate
    if (minResale > depreciatedValue):
        depreciatedValue = minResale
    return depreciatedValue

depreciationRate = 0.7
year = int(input("Enter the starting year: "))
value = float(input("Enter the starting value of the car: "))
minResale = float(input("Enter the minimum resale value of the car: "))

print(f"Car is bought for £{round(value, 2)}. Minimum resale value is £{round(minResale, 2)}")
while (value > minResale):
    value = depreciate(value, depreciationRate, minResale)
    print(f"{year}: £{round(value, 2)}")
    year += 1