import unittest
from undirected_graph import UndirectedGraph
from directed_graph import DirectedGraph
from graph import Graph

class GraphTest(unittest.TestCase):

    def test_empty_graph(self):
        graph_und = UndirectedGraph(5)
        self.assertEqual(graph_und.edge, 0)
        self.assertEqual(graph_und.adj_list, [[], [], [], [], []])
        graph_dir = DirectedGraph(4)
        self.assertEqual(graph_dir.edge, 0)
        self.assertEqual(graph_dir.adj_list, [[], [], [], []])


    def test_edge_added_directed(self):
        graph = DirectedGraph(7)
        graph.add_edge(2, 9)
        self.assertEqual(graph.edge, 0)
        self.assertEqual(graph.adj_list[2], [])
        self.assertNotEqual(len(graph.adj_list), 9)
        graph.add_edge(0, 1)
        graph.add_edge(0, 5)
        graph.add_edge(6, 0)
        graph.add_edge(6, 4)
        graph.add_edge(2, 3)
        self.assertEqual(graph.adj_list[2], [3])
        self.assertEqual(graph.adj_list[3], [])
        graph.add_edge(3, 2)
        self.assertEqual(graph.adj_list[2], [3])
        self.assertEqual(graph.adj_list[3], [2])
        graph.add_edge(2, 0)
        graph.add_edge(3, 5)
        graph.add_edge(4, 2)
        graph.add_edge(4, 3)
        graph.add_edge(5, 4)
        self.assertEqual(graph.edge, 11)

    def test_edge_added_undirected(self):
        graph = UndirectedGraph(7)
        graph.add_edge(2, 9)
        self.assertEqual(graph.edge, 0)
        self.assertEqual(graph.adj_list[2], [])
        self.assertNotEqual(len(graph.adj_list), 9)
        graph.add_edge(0, 1)
        graph.add_edge(0, 5)
        graph.add_edge(6, 0)
        graph.add_edge(6, 4)
        graph.add_edge(2, 3)
        self.assertEqual(graph.edge, 5)
        self.assertEqual(graph.adj_list[3], [2])
        self.assertEqual(graph.adj_list[2], [3])
        graph.add_edge(3, 2)
        self.assertEqual(graph.edge, 5)
        graph.add_edge(2, 0)
        graph.add_edge(3, 5)
        graph.add_edge(4, 2)
        graph.add_edge(4, 3)
        graph.add_edge(5, 4)
        self.assertEqual(graph.edge, 10)

    def test_vertex_added(self):
        graph = Graph(2)
        self.assertEqual(graph.vertices, 2)
        graph.add_vertex()
        self.assertEqual(graph.vertices, 3)

    def test_degree_undirected(self):
        graph = UndirectedGraph(7)
        graph.add_edge(0, 1)
        graph.add_edge(0, 5)
        self.assertEqual(graph.degree(0), 2)

    def test_out_degree_directed(self):
        graph = DirectedGraph(7)
        graph.add_edge(0, 1)
        graph.add_edge(0, 5)
        self.assertEqual(graph.out_degree(0), 2)

    def test_in_degree_directed(self):
        graph = DirectedGraph(7)
        graph.add_edge(0, 1)
        graph.add_edge(0, 5)
        self.assertEqual(graph.in_degree(0), 0)
        self.assertEqual(graph.in_degree(1), 1)
        self.assertEqual(graph.in_degree(1), 1)

    def test_max_degree_directed(self):
        graph = DirectedGraph(7)
        graph.add_edge(0, 1)
        graph.add_edge(2, 1)
        self.assertEqual(graph.max_degree(), 2)

    def test_max_degree_undirected(self):
        graph = UndirectedGraph(7)
        graph.add_edge(0, 1)
        graph.add_edge(0, 3)
        graph.add_edge(0, 5)
        self.assertEqual(graph.max_degree(), 3)

    def test_average_degree(self):
        graph = DirectedGraph(3)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)
        self.assertEqual(graph.average_degree(), 2)
        graph = UndirectedGraph(3)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)
        self.assertEqual(graph.average_degree(), 2)

    def test_numbers_of_self_loop(self):
        graph = UndirectedGraph(4)
        graph.add_edge(2, 2)
        graph.add_edge(3, 3)
        self.assertEqual(graph.numbers_of_self_loop(), 2)
        graph = DirectedGraph(4)
        graph.add_edge(2, 2)
        graph.add_edge(3, 3)
        self.assertEqual(graph.numbers_of_self_loop(), 2)

    def test_dfs_undirected(self):
        graph = UndirectedGraph(7)
        graph.add_edge(0, 6)
        graph.add_edge(0, 2)
        graph.add_edge(0, 1)
        graph.add_edge(0, 5)
        graph.add_edge(6, 4)
        graph.add_edge(4, 5)
        graph.add_edge(4, 3)
        graph.add_edge(5, 3)
        self.assertEqual(graph.dfs(0), [None, 0, 0, 5, 6, 4, 0])

    def test_bfs_undirected(self):
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

    def test_dfs_directed(self):
        graph = DirectedGraph(7)
        graph.add_edge(0, 6)
        graph.add_edge(0, 2)
        graph.add_edge(0, 1)
        graph.add_edge(0, 5)
        graph.add_edge(6, 4)
        graph.add_edge(4, 5)
        graph.add_edge(4, 3)
        graph.add_edge(5, 3)
        self.assertEqual(graph.dfs(0), [None, 0, 0, 5, 6, 4, 0])

    def test_bfs_directed(self):
        graph = DirectedGraph(6)
        graph.add_edge(0, 2)
        graph.add_edge(0, 1)
        graph.add_edge(0, 5)
        graph.add_edge(2, 1)
        graph.add_edge(2, 3)
        graph.add_edge(2, 4)
        graph.add_edge(4, 3)
        graph.add_edge(5, 3)
        self.assertEqual(graph.bfs(0), [None, 0, 0, 2, 2, 0])