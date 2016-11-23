import os


def dfs_tree_pre(root):
    print root
    if root.left:
        dfs_tree_pre(root.left)
    elif root.right:
        dfs_tree_pre(root.right)


def dfs_graph(vertex, visited):
    visited.add(vertex)
    print vertex
    for ver in vertex.adj_list:
        if ver not in visited:
            visited.add(ver)
            dfs_graph(ver, visited)


def find_cycles(vertex, visited, edge_to):
    visited.add(vertex)
    for ver in vertex.adj_list:
        if ver is not visited:
            visited.add(ver)
            dfs_graph(ver)
            edge_to[ver] = vertex
        elif ver is visited and edge_to.get(ver) != ver:
            return True
    return False


def dfs_print_path(root_path):
    list_dir = os.listdir(root_path)
    for file in list_dir:
        path = root_path+file
        if os.path.isfile(path):
            print path
        else:
            path += "/"
            dfs_print_path(path)

if __name__ == '__main__':
    root = "/home/gianluca/Downloads/"
    dfs_print_path(root)
