def mergeSort(arr):
    if (len(arr)<=1):
        return arr
    else:
        mid = len(arr)//2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else :
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
arr = [1, 6, 7, 8, 2, 50, 32]
sorted_array = mergeSort(arr)
print(sorted_array)