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
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

"""

def find_kth_from_end(linked_list, k):
    temp = linked_list.head
    linked_list.head = linked_list.tail
    linked_list.tail = temp

    after = temp.next
    before = None

    while temp is not None:
        after = temp.next
        temp.next = before
        before = temp
        temp = after


    slow = linked_list.head
    fast = linked_list.head
    for i in range(1, k):
        if fast is None:
            return None
        fast = fast.next
        slow = slow.next
    return slow
"""

def find_kth_from_end(ll, k):
    # 1. Initialize two pointers, 'slow' and 'fast',
    # both pointing to the starting node of the linked list
    slow = fast = ll.head

    # 2. Move 'fast' pointer 'k' positions ahead.
    for _ in range(k):
        # 2.1 if at some point during these 'k' movements
        # the 'fast' pointer reaches the end of the list,
        # then it means the list has less than 'k' nodes,
        # thus, returning None
        if fast is None:
            return None

        # 2.2 move 'fast' pointer to the next node.
        fast = fast.next

    # 3. Now we move both 'slow' and 'fast' pointers one node at a time
    # until the 'fast' pointer reaches the end of the list. Since the 'fast'
    # pointer is already 'k' nodes ahead of the 'slow' pointer, by the time 'fast'
    # reaches the end of the list, 'slow' will be at the kth node from the end.

    while fast:
        slow = slow.next
        print("slow value", slow.value)
        fast = fast.next
        if fast is not None:
            print("fast value", fast.value)
        else:
            print("fast is None!")
    # return 'slow' pointer, which is now pointing to the kth node from the end
    # (linked list length minus k)
    return slow






my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)
print(result)  # Output: 4