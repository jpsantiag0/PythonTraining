class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
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
            self.tail.next = new_node # new node where next is None
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True


    def pop(self):
        #if self.head is None:
        #    print("nothing to pop out, LinkedList is empty")

        if self.length == 0:
            return None
        # elif self.tail.next is None:
        #    self.head = None
        #    self.tail = None
        pre = self.head
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp


my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.print_list()

my_linked_list.prepend(1)
my_linked_list.print_list()

# (3) Items - Returns Node 3 (object)
print(my_linked_list.pop())
# (2) Items - Returns Node 2 (object)
print(my_linked_list.pop())
# (1) Item - Returns Node 1 (object)
print(my_linked_list.pop())
# (0) Items - Returns None
print(my_linked_list.pop())

my_linked_list.prepend(3)
my_linked_list.print_list()