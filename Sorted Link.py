import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append a new node with the given data to the linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        """Display the contents of the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def selection_sort(self):
        """Sort the linked list in ascending order using selection sort."""
        if not self.head:
            return
        
        current = self.head
        while current:
            # Find the smallest node in the remaining list
            smallest = current
            next_node = current.next
            while next_node:
                if next_node.data < smallest.data:
                    smallest = next_node
                next_node = next_node.next
            
            # Swap data between the current node and the smallest node
            current.data, smallest.data = smallest.data, current.data
            current = current.next

# Create a linked list
linked_list = LinkedList()

# Add 1000 nodes with random numbers between -1000 and 1000
for k in range(100):
    random_number = random.randint(-1000, 1000)
    linked_list.append(random_number)

# Optional: Display the unsorted linked list
print("Unsorted Linked List:")
linked_list.display()

# Sort the linked list using selection sort
linked_list.selection_sort()

# Display the sorted linked list
print("\nSorted Linked List:")
linked_list.display()
