import os
import sys

"""This method is created to find all files and directories, given a specific path. Optionally, your can use -name flag
to search only the files that match to a specific name"""


def find(path, option=None, filename=None):
    """this method uses a bfs approach to resolve to the problem of finding all files and directories."""
    if not os.path.exists(path):
        return "Path doesn't exist or wrong: please try again"
    queue = []
    queue.append(path)
    paths_list = []
    while len(queue) > 0:
        queue_element = queue.pop(0)
        adj_list = os.listdir(queue_element)
        if len(adj_list) != 0:
            for adj in adj_list:
                if filename is not None and option == "-name":
                    if os.path.isfile(os.path.join(queue_element, adj)) and adj == filename:
                        paths_list.append(os.path.join(queue_element, adj))
                    elif os.path.isdir(os.path.join(queue_element, adj)):
                        queue.append(os.path.join(queue_element, adj))
                elif filename is None and option is None:
                    if os.path.isfile(os.path.join(queue_element, adj)):
                        paths_list.append(os.path.join(queue_element, adj))
                    elif os.path.isdir(os.path.join(queue_element, adj)):
                        queue.append(os.path.join(queue_element, adj))
                        paths_list.append(os.path.join(queue_element, adj))
    paths_list.sort()
    for path in paths_list:
        print path

if __name__ == '__main__':
    find(str(sys.argv[1]), option=str(sys.argv[2]), filename=str(sys.argv[3]))
    # print find("/home/gianluca/projects/exercises/", None, None)
    # print find("/home/gianluca/projects/exercises/", "-name", "tree.py")
