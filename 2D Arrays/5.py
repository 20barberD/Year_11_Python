def transpose(array):
    newArray = []
    for i in array[0]:
        newArray.append([])
    print(newArray)
    for row in range(0, len(array[0])):
        for column in range(0, len(array)):
            print(array[row][column])
            newArray[row].append(array[column][row])
    return newArray

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]

print(transpose(matrix))