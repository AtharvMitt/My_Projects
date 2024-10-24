class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value>temp.value:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right

            else:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if temp.value == value:
                return True
            else:
                if temp.value > value:
                    temp = temp.left
                    continue
                else:
                    temp = temp.right
                    continue
        return False

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)

print(my_tree.contains(3))