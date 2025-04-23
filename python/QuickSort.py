def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr  if x > pivot]
    return quicksort(left)+middle+quicksort(right)
arr = [1, 10, 14, 8, 7, 23]
print("Unsorted Array: ", arr)
new_arr = quicksort(arr)
print("Sorted Array: ", new_arr)