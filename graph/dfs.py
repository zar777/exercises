# from undirected_graph import Graph
#
# class DepthFirstSearch(Graph):
#     """class that inherit all graph methods and it has an array of the neighbors at the end of the dfs"""
#     def __init__(self, v):
#         super(DepthFirstSearch, self).__init__(v)
#         self.edge_to = [None] * v
#
#     def dfs(self, vertex):
#         """depth first search algorithm"""
#         self.marked[vertex] = True
#
#         for adj in self.adj_list[vertex]:
#             if self.marked[adj] is not True:
#                 self.dfs(adj)
#                 self.edge_to[adj] = vertex
#
#
# if __name__ == '__main__':
#     graph = DepthFirstSearch(7)
#     print graph.adj_list
#     print graph.vertices
#     print graph.adj_list
#     print graph.vertices
#     # graph.add_vertex()
#     print graph.vertices
#     print graph.adj_list
#     print len(graph.adj_list)
#     # graph.add_edge(2, 9)
#     print graph.adj_list
#     graph.add_edge(0, 6)
#     graph.add_edge(0, 2)
#     graph.add_edge(0, 1)
#     graph.add_edge(0, 5)
#     graph.add_edge(6, 4)
#     graph.add_edge(4, 5)
#     graph.add_edge(4, 3)
#     graph.add_edge(5, 3)
#     # graph.add_edge(0, 2)
#     # graph.add_edge(1, 4)
#     # graph.add_edge(5, 2)
#     # graph.add_edge(0, 3)
#     # graph.add_edge(0, 4)
#     # graph.add_edge(0, 5)
#     # graph.__str__()
#     print graph.adj_list
#     graph.dfs(0)
#     print graph.edge_to