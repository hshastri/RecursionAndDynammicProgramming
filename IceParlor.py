from BinarySearch import *
from MergeSort import *
import math

def copyArr(arr):
    arrCopy = []
    for i in range(0, len(arr)):
        arrCopy.append(arr[i])
    return arrCopy

def iceParlor(menu, amount):
    tempArr = copyArr(menu)
    MergeSort(tempArr)
    indices = []
    #print(tempArr)

    for i in range(0, len(menu)):
        complement = amount - tempArr[i]
        location = BinarySearchIterative2(tempArr, complement, i + 1, len(menu) - 1)
        #location will return either an index or -1
        if location != -1:
            index1 = menu.index(tempArr[i])
            index2 = menu.index(tempArr[location])
            indices.append((min(index1, index2), max(index1, index2)))

    return indices

def main():
    menu = [4, 8, 1, 6, 2]
    amount = 10
    print(iceParlor(menu, amount))
    print((menu[1] + menu[4]))
    print(menu[0] + menu[3])

if __name__ == '__main__':
     main()