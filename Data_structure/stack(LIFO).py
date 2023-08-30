

#LIFO(last e jeta push hobe setai pop hobe sobar age)
stack = []  # Initialize an empty list as the stack

# Pushing elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
# Popping elements from the stack
popped_element = stack.pop()
print("Popped element:", popped_element)  # Output: Popped element: 3
print(stack)

# Checking if the stack is empty
is_empty = len(stack) == 0
is_empty = len(stack) == 0
print(is_empty)
if is_empty==False:
    print("Is stack not empty")
else:
    print("Is stack empty?", is_empty) 



# Using Class................................

print("Using Class................................")

class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to represent the stack

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)  # Add an item to the top of the stack

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove and return the top item
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Return the top item without removing it
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

# Example usage:
my_stack = Stack()#object
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Stack:", my_stack.items)
print("Size of the stack:", my_stack.size())

top_item = my_stack.pop()
print("Popped item:", top_item)
print("Stack after popping:", my_stack.items)
