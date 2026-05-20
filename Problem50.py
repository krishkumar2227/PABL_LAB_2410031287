#50.Write an program of stack implementation.
class Stack:
    def __init__(self):
        self.stack = []

    # Push element
    def push(self, item):
        self.stack.append(item)
        print(item, "pushed into stack")

    # Pop element
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print(self.stack.pop(), "popped from stack")

    # Peek top element
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Top element is:", self.stack[-1])

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display stack
    def display(self):
        print("Stack:", self.stack)


# Create stack object
s = Stack()

# Operations
s.push(10)
s.push(20)
s.push(30)

s.display()

s.pop()

s.peek()

s.display()