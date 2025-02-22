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

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node, value):
            if current_node == None:
                return Node(value)
            if value < current_node.value:
                current_node.left = self.__r_insert(current_node.left, value)
            if value > current_node.value:
                current_node.right = self.__r_insert(current_node.right, value)
            return current_node

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def _min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None and current_node.right != None:
                current_node = current_node.right
            elif current_node.left != None and current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self._min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node


    def r_delete(self, value):
        self.__delete_node(self.root, value)

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results




my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)

print(my_tree.contains(3))
print(my_tree.r_contains(5))
print(my_tree.BFS())