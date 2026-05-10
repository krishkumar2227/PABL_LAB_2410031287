#42.Print the ASCII value of each character in a string.
# Print ASCII value of each character in a string

string = input("Enter a string: ")

for ch in string:
    print(ch, "=", ord(ch))