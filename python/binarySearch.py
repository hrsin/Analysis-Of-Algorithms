def binarySearch(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
arr = [1, 5, 6, 10, 13, 15]
target  = 15
index = binarySearch(arr, target)
print("Index of Target Value: ", index)