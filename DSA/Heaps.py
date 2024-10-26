class MaxHeap:
    def __init__(self):
        self.Heap = []

    def _left_child(self, index):
        return 2*index+1

    def _right_child(self, index):
        return 2*index+2

    def _parent(self, index):
        return (index-1) // 2

    def _swap(self, index1, index2):
        self.Heap[index1], self.Heap[index2] = self.Heap[index2], self.Heap[index1]

    def insert(self, value):
        self.Heap.append(value)
        current = len(self.Heap) - 1
        while current > 0 and self.Heap[current] > self.Heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.Heap)) and self.Heap[left_index] > self.Heap[max_index]:
                max_index = left_index
            if (right_index < len(self.Heap)) and self.Heap[right_index] > self.Heap[max_index]:
                max_index = right_index
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def remove(self):
        if len(self.Heap) == 0:
            return None
        if len(self.Heap) == 1:
            return self.Heap.pop()
        max_value = self.Heap[0]
        self.Heap[0] = self.Heap.pop()
        self._sink_down(0)
        return max_value




    def print_heap(self):
        print(self.Heap)

my_heap = MaxHeap()
my_heap.insert(95)
my_heap.insert(75)
my_heap.insert(80)
my_heap.insert(55)
my_heap.insert(60)
my_heap.insert(50)
my_heap.insert(65)
my_heap.print_heap()
my_heap.remove()
my_heap.print_heap()
my_heap.remove()
my_heap.print_heap()