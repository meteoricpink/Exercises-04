"""
Exercise template for exercise 04 linked lists
"""


# singly linked list
# node class of the singly linked list
class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # pointer to the next node

    def __str__(self):
        return str(self.data)


# Singly linked list class
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        # Create the new node the pointer is set to None through the constructor of the SLLNode class
        node = SLLNode(data)
        if self.head is None:  # if the list is empty, the new node is the head
            self.head = node
        else:  # if it is not empty, we need to find the last node and append the new node
            current = self.head
            while current.next is not None:
                current = current.next
            # set the pointer of the last node to the new node
            current.next = node
        self.size += 1  # increase the size of the list

    def get_size(self):
        return self.size

    # string representation of the linked list
    def __str__(self):
        return str([node for node in self])

    # iteration function without this function we can not iterate over the list
    def __iter__(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    def clear(self):
        self.head = None
        self.size = 0

    def get_data(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current.data
            current = current.next
        return False

    def insert_node(self, prev_data, new_data):
        current = self.head
        while current is not None:
            if current.data == prev_data:
                new_node = SLLNode(new_data)
                new_node.next = current.next
                current.next = new_node
                self.size += 1
                return True
            current = current.next
        return False

    def delete_node(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next


my_list = SinglyLinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)

print(my_list)

print(my_list.get_size())

my_list.insert_node(2, 4)

print(my_list)

print(my_list.get_data(4))

my_list.delete_node(2)

print(my_list)

my_list.clear()

print(my_list)



"""
Exercise part 5
Implement a doubly linked list according to the exercise sheet.
You can copy the code from the singly linked list and modify it.
"""

class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = DLLNode(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def prepend(self, data):
        node = DLLNode(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def insert_node(self, prev_node_data, new_node_data):
        node = DLLNode(new_node_data)
        current = self.head
        while current is not None:
            if current.data == prev_node_data:
                node.next = current.next
                node.prev = current
                if current.next is not None:
                    current.next.prev = node
                current.next = node
                self.size += 1
                return
            current = current.next

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_data(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current.data
            current = current.next
        return None

    def delete_node(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is None:
                    self.head = current.next
                else:
                    current.prev.next = current.next
                if current.next is None:
                    self.tail = current.prev
                else:
                    current.next.prev = current.prev
                self.size -= 1
                return
            current = current.next

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __str__(self):
        return str([node for node in self])

    def get_size(self):
        return self.size


my_list = DoublyLinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)

print(my_list)

print(my_list.get_size())

my_list.insert_node(2, 4)

print(my_list)

print(my_list.get_data(4))

my_list.delete_node(2)

print(my_list)

my_list.clear()

print(my_list)


"""
Exercise Part 6 and 7:
Complete the classes below to implement a stack and queue data structure. You are free to use built-in
methods but you have to complete all methods below. Always return the correct data type according
to the exercise sheet
"""


class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    def size(self):
        return len(self.stack)

my_stack = MyStack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print(my_stack.size())

print(my_stack.top())

my_stack.pop()


class MyQueue:

    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)

    def show_left(self):
        if not self.is_empty():
            return self.items[0]

    def show_right(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

my_queue = MyQueue()

my_queue.push(1)
my_queue.push(2)
my_queue.push(3)

my_queue.pop()

print(my_queue.show_left())

print(my_queue.show_right())

print(my_queue.size())