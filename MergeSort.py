import math

def MergeSort(list):
    #Split list
    newList = [list]
    split = False
    while not split:
        for index in range(len(newList)):
            thing = newList[index]
            if len(newList) == len(list):
                split = True
            elif len(thing) % 2 == 0:
                del newList[index]
                newList.insert(index, thing[:math.ceil(len(thing)/2)])
                newList.insert(index+1, thing[math.ceil(len(thing)/2):])
                print(newList)
    #Compare pairs
    step = 1
    while len(list) > 2 ** step:
        size = 2 ** step
        for i in range(0, len(newList), size):
            #[[3], [1]]
            #[[1, 3], [3, 8]]
            list1 = newList[i]
            list2 = newList[i+1]
            combinedList = []
            if list2[0] > list1[-1]:
                combinedList = list1 + list2
            elif list1[0] > list2[-1]:
                combinedList = list2 + list1
        step += 1
    return newList

print(MergeSort([3, 1, 3, 8, 5, 1, 7, 4]))