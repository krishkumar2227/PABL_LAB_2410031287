#48.Print a square of stars recursively (n×n).
# Function to print one row
def print_cols(n):
    if n == 0:
        return
    
    print("*", end=" ")
    print_cols(n - 1)


# Function to print square recursively
def print_rows(n):
    if n == 0:
        return
    
    print_cols(n)
    print()   # Move to next line
    
    print_rows(n - 1)


# Input
n = int(input("Enter size of square: "))

# Function call
print_rows(n)