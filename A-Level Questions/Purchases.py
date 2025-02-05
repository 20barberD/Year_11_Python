#Task 13
def formatAsMoney(number):
    text = ""
    split = str(round(number, 2)).split('.')
    text += f"{split[0]}.{split[1]}"
    if len(split[1]) < 2:
        for i in range(len(split[1]), 0, -1):
            text += "0"
    return text

def printReceipt(purchases, discounts):
    totalSpent = 0
    receiptText = ""
    for i in range(0, len(purchases)):
        purchase = purchases[i]
        receiptText += f"{purchase[0]} £{formatAsMoney(purchase[2])}\n"
        if discounts[i] != 0:
            discount = purchase[2] * (1-(discounts[i]/100))
            totalSpent += discount
            receiptText += f"-£{formatAsMoney(purchase[2]-discount)} discount\n"
        else:
            totalSpent += purchase[2]
    receiptText += "------------------\n"
    receiptText += f"TOTAL: £{formatAsMoney(totalSpent)}"
    return receiptText

def gardeningDiscount(purchases):
    discounts = []
    decoratingTotalSpent = 0
    for purchase in purchases:
        if purchase[1] == "Decorating": #If decorating product
            decoratingTotalSpent += purchase[2] #Add amount spent to total spent on decorating products
    if decoratingTotalSpent >= 20.00: #If £20 or more spent on decorating products
        for i in range(0, len(purchases)):
            if purchases[i][1] == "Gardening": #If gardening product
                discounts.append(10) #Add 10% discount to this item on the discounts array
            else:
                discounts.append(0) #Add no discount to this item on the discounts array
    return discounts #Return discounts for each item

purchases = [
    ["Matt Pink Paint", "Decorating", 6.99],
    ["Floral Wallpaper", "Decorating", 7.99],
    ["Magnolia Gloss Paint", "Decorating", 5.49],
    ["Weed Killer", "Gardening", 2.99],
    ["Picture Frame", "Decorating", 8.99],
    ["Plug Socket", "Electrics", 6.99],
    ["Doorbell", "ELectrics", 15.99],
    ["Matt White Paint", "Decorating", 4.99],
    ["Tiles", "Decorating", 19.99],
    ["Grass Seed", "Gardening", 1.99],
    ["Lawn Mower", "Gardening", 129.99]
]
discounts = gardeningDiscount(purchases)
receipt = printReceipt(purchases, discounts)
print(receipt)

print(formatAsMoney(19.2))