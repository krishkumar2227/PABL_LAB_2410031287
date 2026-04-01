#2.Given an array arr[]. Your task is to find the minimum and maximum elements in the array.
def find_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
            
    return min_val, max_val


# Example
arr = [3, 5, 1, 9, 2]
mn, mx = find_min_max(arr)

print("Minimum:", mn)
print("Maximum:", mx)

