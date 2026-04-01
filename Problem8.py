#8.Given a sorted array of distinct integers and a target value, return the index if the target is found.If not,return the index where it would be if it were inserted in order.
def search_insert(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left   # insertion position


# Example
arr = [1, 3, 5, 6]

print(search_insert(arr, 5))  # 2
print(search_insert(arr, 2))  # 1
print(search_insert(arr, 7))  # 4