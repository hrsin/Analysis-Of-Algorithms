def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [10, 8, 13, 4, 15, 5]
print("Unsorted array: ", arr)
selectionSort(arr)
print("Sorted Array: ", arr)