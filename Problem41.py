#41.Print Factorial of each number from 1 to n.
n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i
    print("Factorial of", i, "=", fact)