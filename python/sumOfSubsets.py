def sum_of_subsets(arr, target):
    result = []
    
    def backtrack(start, curr_subset, curr_sum):
        if curr_sum == target:
            result.append(list(curr_subset))
            return
        if curr_sum > target or start == len(arr):
            return
        for i in range(start, len(arr)):
            curr_subset.append(arr[i])
            backtrack(i + 1, curr_subset, curr_sum + arr[i])
            curr_subset.pop()

    backtrack(0, [], 0)
    return result

arr = [10, 7, 5, 18, 12, 20, 15]
target = 35
subsets = sum_of_subsets(arr, target)
print("Subsets with sum", target, "->", subsets)
