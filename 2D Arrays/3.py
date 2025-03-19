def sumOfNumbersInRow(array, rowIndex):
    sum = 0
    for number in array[rowIndex]:
        sum += number
    return sum

numbers = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]
print(sumOfNumbersInRow(numbers, 1))