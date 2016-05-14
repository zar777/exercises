import unittest
from undirected_graph import UndirectedGraph

class GraphTest(unittest.TestCase):

    def test_empty_graph(self):
        pass

    def test_edge_added(self):
        pass

    def test_vertex_added(self):
        pass

    def test_degree(self):
        pass

    def test_max_degree(self):
        pass

    def test_average_degree(self):
        pass

    def test_numbers_of_self_loop(self):
        pass

    def test_dfs(self):
        graph = UndirectedGraph(7)
        graph.add_edge(0, 6)
        graph.add_edge(0, 2)
        graph.add_edge(0, 1)
        graph.add_edge(0, 5)
        graph.add_edge(6, 4)
        graph.add_edge(4, 5)
        graph.add_edge(4, 3)
        graph.add_edge(5, 3)
        self.assertEqual(graph.dfs(0) , [None, 0, 0, 5, 6, 4, 0])

    def test_bfs(self):
        graph = UndirectedGraph(6)
        graph.add_edge(0, 2)
        graph.add_edge(0, 1)
        graph.add_edge(0, 5)
        graph.add_edge(2, 1)
        graph.add_edge(2, 3)
        graph.add_edge(2, 4)
        graph.add_edge(4, 3)
        graph.add_edge(5, 3)
        self.assertEqual(graph.bfs(0),  [None, 0, 0, 2, 2, 0])