# =================================Linked=List==================================
# 1.Data structure = Linked_list
# 2.Problem - Reversing a Linked List

class Node():
    def __init(self, num):
        self.data = num
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head in None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    def show_elements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def length(self):
        result = 0
        current = self.head
        while current is not None:
            result += 1
            current = current.next
        return result

    def get_element(self, position):
        i = 0
        current = self.head
        while current is not None:
            if i == position:
                return current.data
            current = current.next
            i += 1
        return None


def reverse(linked_list):
    if linked_list.head is None:
        return

    current_node = linked_list.head
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
