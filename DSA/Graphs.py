class Graphs:
    def __init__(self):
        self.adj_list = {}
        self.length = 0


    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for i in self.adj_list:
            print(i , ":" , self.adj_list[i])

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, v1):
        if v1 in self.adj_list.keys():
            for i in self.adj_list[v1]:
                self.adj_list[i].remove(v1)
            del self.adj_list[v1]
            return True
        return False
    

my_graph = Graphs()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.print_graph()
print()
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("B", "C")
my_graph.print_graph()
print()
my_graph.remove_edge("A", "B")
my_graph.remove_edge("A", "D")
my_graph.print_graph()
print()
my_graph.remove_vertex("C")
my_graph.print_graph()