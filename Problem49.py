#49.Move All Zeros to End
def move_zeros(arr):
    index = 0

    # Move non-zero elements forward
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[index] = arr[i]
            index += 1

    # Fill remaining positions with 0
    while index < len(arr):
        arr[index] = 0
        index += 1

    return arr


# Example
arr = [1, 0, 2, 0, 4, 0, 5]

result = move_zeros(arr)

print("Array after moving zeros:")
print(result)