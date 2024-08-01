class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def insert_after_node(self, prev_node_data, data):
        current = self.head
        while current:
            if current.data == prev_node_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Node with data {prev_node_data} not found.")

# Create a linked list
linked_list = SinglyLinkedList()

# Append elements
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

# Traverse the list
print("Traverse after append:")
linked_list.traverse()

# Prepend an element
linked_list.prepend(5)

# Traverse the list
print("Traverse after prepend:")
linked_list.traverse()

# Delete an element
linked_list.delete_with_value(20)

# Traverse the list
print("Traverse after deletion:")
linked_list.traverse()

# Get the length of the list
length = linked_list.get_length()
print(f"Length of the list: {length}")

# Find an element
node = linked_list.find(10)
if node:
    print(f"Node found with data: {node.data}")
else:
    print("Node not found")

# Insert after a specific node
linked_list.insert_after_node(10, 15)

# Traverse the list
print("Traverse after insertion:")
linked_list.traverse()
