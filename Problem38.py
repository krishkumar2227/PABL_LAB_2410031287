#38.Rotate an array by one position to the right.
def rotate_right(arr):
    n = len(arr)
    if n == 0:
        return arr

    last = arr[n - 1]          # Step 1
    for i in range(n - 1, 0, -1):   # Step 2
        arr[i] = arr[i - 1]
    arr[0] = last              # Step 3
    
    return arr


# Example
arr = [1, 2, 3, 4, 5]
print(rotate_right(arr))
