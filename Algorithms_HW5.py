# 1. Selection Sort:
# Implement the selection sort algorithm that is sorting in descending order.

def selection(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i+1,len(arr)):
            if arr[j] > arr[max_index]:
                 max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

print(selection([2,1,4,3,6,8]))

# 2. Bubble Sort:
# Implement the bubble sort algorithm that is sorting in descending order.

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i -1):
            if arr[j+1] > arr[j]:
                arr[j+1] , arr[j] = arr[j] ,arr[j+1]
    return arr


print(bubble_sort([2, 1, 4, 3, 6, 8]))

# 3. Insertion Sort:
# Implement the insertion sort algorithm that is sorting in descending order.

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
print(insertion_sort([1,2,3,4,5,6,7,8]))

# 3. Merge Sort:
# Implement the merge sort algorithm that is sorting in descending order.

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1

myList = [2, 1, 4, 3, 5, 7, 6, 8]
(mergeSort(myList))
print(myList)