def carpetCost(width, length, priceOfCarpet):
    area = width * length
    return (priceOfCarpet * area) + (3 * area) + 50

print(carpetCost(7, 6, 17))