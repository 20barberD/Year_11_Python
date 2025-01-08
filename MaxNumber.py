def MaxNumbers(*numbers):
    highestNumber = numbers[0]
    for number in numbers:
        if number > highestNumber:
            highestNumber = number
    return highestNumber

print(MaxNumbers(1, 6, 5, 2, 3, 4))