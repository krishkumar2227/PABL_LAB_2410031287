#44. Count how many times a number appears consecutively in an array.
arr = [1, 1, 1, 2, 2, 3, 1, 1]

count = 1

for i in range(len(arr) - 1):
    if arr[i] == arr[i + 1]:
        count += 1
    else:
        print(arr[i], "appears consecutively", count, "times")
        count = 1

# for last element/group
print(arr[-1], "appears consecutively", count, "times")
