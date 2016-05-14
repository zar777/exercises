from graph import Graph

class UndirectedGraph(Graph):
    def __init__(self, v):
        super(UndirectedGraph, self).__init__(v)

    def add_edge(self, v, w):
        """add an edge between two vertices: update the adjacent list of v and w respectively and the number of edges
        in graph"""
        if v < len(self.adj_list) and w < len(self.adj_list):
            if v not in self.adj_list[w] and w not in self.adj_list[v]:
                if w == v:
                    self.adj_list[v].append(w)
                else:
                    self.adj_list[v].append(w)
                    self.adj_list[w].append(v)
                self.edge += 1

    def average_degree(self):
        """average degree of the graph"""
        return 2 * self.edge / self.vertices

    def __str__(self):
        vertex = 0
        adj_element = 0
        while vertex < self.vertices:
            while adj_element < len(self.adj_list[vertex]):
                print '%s' % vertex + ' ---- ' + '%s' % self.adj_list[vertex][adj_element]
                adj_element += 1
            vertex += 1
            adj_element = 0

if __name__ == '__main__':
    graph = UndirectedGraph(7)
    print graph.adj_list
    print graph.vertices
    print graph.adj_list
    print graph.vertices
    # graph.add_vertex()
    print graph.vertices
    print graph.adj_list
    print len(graph.adj_list)
    graph.add_edge(0, 6)
    graph.add_edge(0, 2)
    graph.add_edge(0, 1)
    graph.add_edge(0, 5)
    graph.add_edge(6, 4)
    graph.add_edge(4, 5)
    graph.add_edge(4, 3)
    graph.add_edge(5, 3)
    # graph.add_edge(0, 2)
    # graph.add_edge(1, 4)
    # graph.add_edge(5, 2)
    # graph.add_edge(0, 3)
    # graph.add_edge(0, 4)
    # graph.add_edge(0, 5)
    # graph.__str__()
    # print graph.degree(3)
    # print graph.adj_list
    # print graph.max_degree()
    # print graph.average_degree()
    # print graph.numbers_of_self_loop()
    print graph.adj_list
    print graph.bfs(0)
    print graph.dfs(0)
    # graph.dfs(0)
