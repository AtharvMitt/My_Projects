class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Doubly_Linked_List:
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
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length==0:
            return None
        temp = self.head
        if self.length==1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < index/2:
            temp = self.head
            for i in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for i in range(self.length-1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == self.length:
            return self.append(value)
        if index == 0:
            return self.prepend(value)
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next
        new_node.next = after
        new_node.prev = before
        after.prev = new_node
        before.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == (self.length-1):
            return self.pop()
        if index == 0:
            return self.pop_first()
        temp = self.get(index)
        temp.next = None
        temp.prev = None
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        self.length -= 1
        return temp


my_doubly_linked_list = Doubly_Linked_List(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.set_value(2, 5)
print(my_doubly_linked_list.get(3))
print()
my_doubly_linked_list.print_list()
print()
my_doubly_linked_list.remove(1)
my_doubly_linked_list.print_list()
