def BubbleSort(list):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(list)):
            if list[i-1] > list[i]:
                sorted = False
                itemTemp = list[i-1]
                list[i-1] = list[i]
                list[i] = itemTemp
    return list

print(BubbleSort([7, 1, 3, 4, 2, 99, 5, 6, 3, 2, 445, 123, 4, 4, 4, 6, 7, 6, 7, 8, 8]))