#45.Calculate power of a number (xⁿ) using recursion.
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

x = int(input("Enter base number: "))
n = int(input("Enter power: "))

result = power(x, n)

print("Result =", result)
