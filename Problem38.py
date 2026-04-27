#38.Take 5 numbers as input. If the user enters 0, skip it using continue. At the end, print the sum of all non-zero numbers entered.
sum = 0

for i in range(5):
    num = int(input("Enter a number: "))
    
    if num == 0:
        continue
    
    sum += num

print("Sum of non-zero numbers:", sum)