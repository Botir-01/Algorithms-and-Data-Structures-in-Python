# Write a function to reverse a linked list
# A linked list is a data structure for storing a sequence of elements.
# It is data with some structure (the sequence).

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    def show_elements(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def get_length(self):
        current_node = self.head
        result = 0
        while current_node is not None:
            result += 1
            current_node = current_node.next
        return result

    def get_element(self, position):
        i = 0
        current_node = self.head
        while current_node is not None:
            if i == position:
                return current_node.data
            i += 1
            current_node = current_node.next
        return -1


list1 = LinkedList()
list1.head = Node(2)
list1.head.next = Node(3)
list1.head.next.next = Node(4)


# Reversing a linked list
def reverse(linked_list):
    # The head of the linked list is None, return
    if linked_list.head is None:
        return
    # Store the current node
    current_node = linked_list.head

    # Create a variable to store the previous node
    prev_node = None
    while current_node is not None:
        # Track the next node
        next_node = current_node.next

        # Modify the current node
        current_node.next = prev_node

        # Update prev and current
        prev_node = current_node
        current_node = next_node

    linked_list.head = prev_node