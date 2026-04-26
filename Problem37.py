#Print first n terms of a geometric progression (a, r).
# Input
a = int(input("Enter first term (a): "))
r = int(input("Enter common ratio (r): "))
n = int(input("Enter number of terms (n): "))

# Print GP
term = a
for i in range(n):
    print(term, end=" ")
    term = term * r