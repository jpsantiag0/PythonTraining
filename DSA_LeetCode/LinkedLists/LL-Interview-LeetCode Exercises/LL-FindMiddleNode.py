class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def find_middle_node(self):
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast.next is not None:
            fast = fast.next
            slow = slow.next
            if fast.next is not None:
                fast = fast.next

        return slow




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)

print(my_linked_list.find_middle_node().value)
