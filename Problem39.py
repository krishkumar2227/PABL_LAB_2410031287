#39.# Take input for number of elements and print only those greater than a given value k.
n = int(input("Enter number of elements: "))

# Take array input
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

# Take value of k
k = int(input("Enter value of k: "))

print("Elements greater than", k, "are:")

# Check and print elements greater than k
for i in arr:
    if i > k:
        print(i)