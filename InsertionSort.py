def InsertionSort(list):
    newList = []
    for item in list:
        if len(newList) == 0:
            newList.append(item)
        else:
            print(newList)
            for otherItem in range(len(newList)):
                if item > newList[otherItem]:
                    if otherItem == len(newList)-1 or newList[otherItem+1] > item: #check if it is highest in the list
                        newList.insert(otherItem+1, item)
                        break
                elif newList[otherItem] > item:
                    newList.insert(otherItem, item)
                    break
    return newList

print(InsertionSort([7, 1, 3, 4, 2, 99, 5, 6, 3, 2, 445, 123, 4, 4, 4, 6, 7, 6, 7, 8, 8]))