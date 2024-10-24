class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def _hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def set_item(self, key, value):
        index = self._hash(key)
        if self.data_map[index] == None:
            self.data_map[index]=[]
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i in self.data_map[index]:
                if i[0] == key:
                    return i[1]
        return None

    def keys(self):
        L=[]
        for i in self.data_map:
            if i is None:
                continue
            else:
                for j in i:
                    L.append(j[0])
        return L


my_hash_table = HashTable()
my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 50)
my_hash_table.set_item("dispenser", 1000000000)
print(my_hash_table.get_item("bo"))
print()
my_hash_table.print_table()
print()
print(my_hash_table.keys())
