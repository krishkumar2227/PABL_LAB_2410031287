#4.You are given two arrays a[] and b[], return the Union of both the arrays in any order.The union of two array is a collection of all distinct elements present in either of the array.
def union_arrays(a, b):
    return list(set(a) | set(b))   # union of two sets

# Example
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

result = union_arrays(a, b)
print("Union:", result)