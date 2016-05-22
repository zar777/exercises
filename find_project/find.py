import os
import sys

"""this method is created to find all file and directory, given a specific path. Optionally, your can use -name flag
to search only the files that match to a specific name"""


def find(path, option=None, filename=None):
    """this method uses a bfs approach to resolve to the problem of finding all files and directories."""
    if not os.path.exists(path):
        return "Path non corretto o inestitente: si prega di riprovare"
    queue = []
    queue.append(path)
    # marked = [False] * len(list)
    # edge_to = [None] * len(list)
    list = []
    if filename is None and option is None:
        while len(queue) > 0:
            queue_element = queue.pop(0)
            adj_list = os.listdir(queue_element)
            if adj_list is not []:
                for adj in adj_list:
                    if os.path.isfile(queue_element + adj):
                        # print queue_element+adj
                        list.append(queue_element + adj)
                    elif os.path.isdir(queue_element + adj + "/"):
                        queue.append(queue_element + adj + "/")
                        # print queue_element+adj
                        list.append(queue_element + adj)
        list.sort()
        for path in list:
            print path
    elif filename is not None and option == "-name":
        while len(queue) > 0:
            queue_element = queue.pop(0)
            adj_list = os.listdir(queue_element)
            if adj_list is not []:
                for adj in adj_list:
                    if os.path.isfile(queue_element + adj) and adj == filename:
                        # print queue_element+adj
                        list.append(queue_element + adj)
                    elif os.path.isdir(queue_element + adj + "/"):
                        queue.append(queue_element + adj + "/")
                        # print queue_element+adj
                        # list.append(queue_element + adj)
        list.sort()
        for path in list:
            print path


if __name__ == '__main__':
    # print 'Number of arguments:', len(sys.argv), 'arguments.'
    # print 'Argument List:', str(sys.argv[1])
    find(str(sys.argv[1]), option=str(sys.argv[2]), filename=str(sys.argv[3]))
    # print find("/home/gianluca/projects/exercises/")
    # print find("/home/gianluca/Downloads/")
    # print find("/home/gianluca/pycharm-community-2016.1.2/")
