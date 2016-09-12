import os


def bsf_tree(root):
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        print current_node
        if root.left:
            queue.append(root.left)
        if root.right():
            queue.append(root.right())


def bfs_graph(vertex):
    queue = [vertex]
    visited = set(vertex)
    while queue:
        current_vertex = queue.pop(0)
        if current_vertex not in visited:
            visited.add(current_vertex)
            print current_vertex
            for ver in current_vertex.adj_list:
                if ver not in visited:
                    queue.append(ver)


def bfs_print_path(root_path):
    queue = [root_path]
    while queue:
        curr_dir = queue.pop(0)
        list_curr = os.listdir(curr_dir)
        for file in list_curr:
            file_path = curr_dir + file
            if os.path.isfile(file_path):
                print file_path
            else:
                file_path += "/"
                queue.append(file_path)


if __name__ == '__main__':
    path = "/home/gianluca/Downloads/"
    bfs_print_path(path)
