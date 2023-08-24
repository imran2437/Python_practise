class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Reference to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty linked list

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)

my_list.display()

# In this code:

#     Node represents an individual element in the linked list. Each node contains a data attribute to store the value of the node and a next attribute to reference the next node in the list.

#     LinkedList is the main class representing the linked list. It has a head attribute that points to the first node in the list.

#     The append method adds a new node with the specified data to the end of the linked list.

#     The display method traverses the linked list and prints its elements.

# In the example usage section, we create a linked list, append three elements (1, 2, and 3), and then display the linked list, which should print "1 -> 2 -> 3 -> None."

# This is a simple example of a singly linked list. Depending on your requirements, you can extend this implementation to include more advanced operations like inserting, deleting, or searching for nodes within the linked list.