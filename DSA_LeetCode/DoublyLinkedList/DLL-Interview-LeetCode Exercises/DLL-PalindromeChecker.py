class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True


    def is_palindrome_v2(self):
        if self.length == 0:
            return True

        temp = self.head
        temp2 = self.tail

        forward_list = []
        backward_list = []
        for _ in range(self.length):
            forward_list.append(temp.value)
            temp = temp.next

        for _ in range(self.length - 1, -1, -1):
            backward_list.append(temp2.value)
            temp2 = temp2.prev

        return forward_list == backward_list

    def is_palindrome(self):
        if self.length <= 1:
            return True

        forward_node = self.head
        backward_node = self.tail

        # Traverse through the first half of the list. We only need to
        # check half because we're comparing two nodes at once: one from
        # the beginning and one from the end.
        for i in range(self.length // 2):
            if forward_node.value != backward_node.value:
                return False

            forward_node = forward_node.next
            backward_node = backward_node.prev
        return True





my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(1)

print('my_dll_1 is_palindrome:')
print( my_dll_1.is_palindrome() )


my_dll_2 = DoublyLinkedList(1)
my_dll_2.append(2)
my_dll_2.append(3)

print('\nmy_dll_2 is_palindrome:')
print( my_dll_2.is_palindrome() )



"""
    EXPECTED OUTPUT:
    ----------------
    my_dll_1 is_palindrome:
    True

    my_dll_2 is_palindrome:
    False

"""

