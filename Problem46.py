#46.Print a triangle of stars recursively (top-down).
def triangle(n):
    if n == 0:   # Base case
        return
    
    print("*" * n)   # Print stars
    triangle(n - 1)  # Recursive call


# Example
triangle(5)
