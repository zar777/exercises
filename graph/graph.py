class Graph(object):
    """this class is created to represent a Graph, passing a number of vertices. it is characterized by:
    number of vertices, number of edge, bag of adjacent elements, and two lists: marked[] represents if the vertices are visited
    and edge_to[], in which is added all edges are visited(after to have executed a visit algorithm)"""
    def __init__(self, v):
        self.vertices = v
        self.edge = 0
        self.adj_list = [[]]
        self.marked = [False] * self.vertices
        self.edge_to = [None] * self.vertices
        while len(self.adj_list) != self.vertices:
            self.adj_list.append([])

    def add_vertex(self):
        """add upload a number of vertices and append a new bag element"""
        self.adj_list.append([])
        self.vertices += 1

    def add_edge(self, v, w):
        """add an edge between two vertices"""
        pass

    def max_degree(self):
       pass

    def average_degree(self):
        """average degree of the graph"""
        return 2 * self.edge / self.vertices

    def numbers_of_self_loop(self):
        count_loop = 0
        vertex = 0
        while vertex < self.vertices:
            if vertex in self.adj_list[vertex]:
                count_loop += 1
            vertex += 1
        return count_loop

    def __str__(self):
        vertex = 0
        adj_element = 0
        while vertex < self.vertices:
            while adj_element < len(self.adj_list[vertex]):
                print '%s' % vertex + ' ----> ' + '%s' % self.adj_list[vertex][adj_element]
                adj_element += 1
            vertex += 1
            adj_element = 0

    def dfs(self, vertex):
        """depth first search algorithm"""
        self.marked[vertex] = True

        for adj in self.adj_list[vertex]:
            if self.marked[adj] is not True:
                self.dfs(adj)
                self.edge_to[adj] = vertex
        return self.edge_to

    def bfs(self, vertex):
        """breadth first search algorithm"""
        queue = []
        queue.append(vertex)
        marked = [False] * self.vertices
        edge_to = [None] * self.vertices
        marked[vertex] = True

        while len(queue) > 0:
            queue_element = queue.pop(0)
            for adj in self.adj_list[queue_element]:
                if marked[adj] is False:
                    queue.append(adj)
                    marked[adj] = True
                    edge_to[adj] = queue_element
        return edge_to
