#7.You are given an integer array arr[]. You need to find the maximum sum of a subarray in the array arrr[].
def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = 0
    
    for num in arr:
        current_sum += num
        
        if current_sum > max_sum:
            max_sum = current_sum
        
        if current_sum < 0:
            current_sum = 0
    
    return max_sum


# Example
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray Sum:", max_subarray_sum(arr))