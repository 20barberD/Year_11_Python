def findLargestNumber(array):
    largestNumber = array[0][0]
    for row in array:
        for number in row:
            if number > largestNumber:
                largestNumber = number
    return largestNumber

numbers = [
    [3, 7, 2],
    [8, 1, 9],
    [4, 6, 5]
]
print(findLargestNumber(numbers))