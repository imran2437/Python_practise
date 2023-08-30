from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)
front = queue.popleft()
print(front)
print("......................")

class Queue:
    def __init__(self):
        self.items = []  # Initialize an empty list to represent the queue

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)  # Add an item to the rear of the queue

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove and return the front item
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]  # Return the front item without removing it
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Example usage:
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Queue:", my_queue.items)
print("Size of the queue:", my_queue.size())

front_item = my_queue.dequeue()
print("Dequeued item:", front_item)
print("Queue after dequeuing:", my_queue.items)
