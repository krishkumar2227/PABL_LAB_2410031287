#5.Given an array arr[]. The task is to find the largest element and return it.
def find_largest(arr):
    max_val = arr[0]
    
    for num in arr:
        if num > max_val:
            max_val = num
            
    return max_val


# Example
arr = [3, 5, 7, 2, 8, 1]
print("Largest element:", find_largest(arr))