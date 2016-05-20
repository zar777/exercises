"""Given a directed graph, design an algorithm to find out whether there is a route between two nodes"""

from graph.directed_graph import DirectedGraph

def find_route(graph, v, w):
    """dfs of v vertex and use the result edge list to define what is the route between v and w: it begins from the last
    element of the route (w) to the first (v) surfing the list in the opposite direction"""
    route = ""
    edge_list = graph.dfs(v)
    if edge_list[w] is not None:
        if edge_list[w] == v:
            return str(v) + " ---> " + str(w)
        else:
            route += str(w)
            while edge_list[w] != v:
                route += " <--- " + str(edge_list[w])
                w = edge_list[w]
            route += " <--- " + str(v)
            return route
    return "Route not present between " + str(v) + " and " + str(w)

if __name__ == '__main__':
    graph = DirectedGraph(7)
    graph.add_edge(0, 6)
    graph.add_edge(0, 2)
    graph.add_edge(0, 1)
    graph.add_edge(0, 5)
    graph.add_edge(6, 4)
    graph.add_edge(4, 5)
    graph.add_edge(4, 3)
    graph.add_edge(5, 3)
    graph.dfs(2)
    print graph.edge_to
    print find_route(graph, 1, 2)