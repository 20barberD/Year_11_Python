#Task 8
import math

def BinarySearch(list, number):
    print(list)
    middle = math.ceil(len(list)/2)
    if len(list) == 1 and number == list[0]:
        return True
    print(number, middle)
    if number == list[middle]:
        return True
    elif number > list[middle]:
        return BinarySearch(list[middle:], number)
    elif list[middle] > number:
        return BinarySearch(list[:middle], number)
    return False

list = [2, 3, 5, 5, 6, 7, 8, 8, 136, 754645623]
print(BinarySearch(list, 136))