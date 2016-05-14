from graph import Graph

class DirectedGraph(Graph):
    def __init__(self, v):
        super(DirectedGraph, self).__init__(v)

    def add_edge(self, v, w):
        """add an edge between two vertices: update the adjacent list of v and w respectively and the number of edges
        in graph"""
        if v < len(self.adj_list) and w < len(self.adj_list):
            if w not in self.adj_list[v]:
                self.adj_list[v].append(w)
                self.edge += 1

    def out_degree(self, vertex):
        """number of vertices Outbound of a given vertex"""
        adj_element = 0
        in_vertex_degree = 0
        while adj_element < len(self.adj_list[vertex]):
            adj_element += 1
            in_vertex_degree += 1
        return in_vertex_degree

    def in_degree(self, vertex):
        """number of vertices Inbound of a given vertex"""
        vertex_degree = 0
        for v in self.adj_list:
            if vertex in v:
                vertex_degree += 1
        return vertex_degree

    def max_degree(self):
        """vertex which have a maximum number of edge represents a max degree of graph"""
        max = 0
        vertex = 0
        while vertex < self.vertices:
            if self.in_degree(vertex) > max:
                max = self.in_degree(vertex)
            vertex += 1
        return max


if __name__ == '__main__':
    graph = DirectedGraph(7)
    print graph.adj_list
    print graph.vertices
    print graph.adj_list
    print graph.vertices
    # graph.add_vertex()
    print graph.vertices
    print graph.adj_list
    print len(graph.adj_list)
    graph.add_edge(2, 9)
    graph.add_edge(0, 1)
    graph.add_edge(0, 5)
    graph.add_edge(6, 0)
    graph.add_edge(6, 4)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 2)
    graph.add_edge(3, 5)
    graph.add_edge(4, 2)
    graph.add_edge(4, 3)
    graph.add_edge(5, 4)
    graph.__str__()
    print graph.adj_list
    print graph.out_degree(3)
    print graph.in_degree(3)
    print graph.adj_list[3]
    print graph.adj_list
    print graph.max_degree()
    print graph.average_degree()
    print graph.numbers_of_self_loop()
    # array = [2, 4, 6]
    # array.append(3)
    # print array