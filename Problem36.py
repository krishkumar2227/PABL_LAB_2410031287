#36.Print pattern of characters (A, AB, ABC, ...) recursively.
def print_pattern(n, current=1):
    if current > n:
        return
    
    # Print characters from A to current
    for i in range(current):
        print(chr(65 + i), end="")
    print()
    
    # Recursive call
    print_pattern(n, current + 1)

# Example usage
n = 5
print_pattern(n)