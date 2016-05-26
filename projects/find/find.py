import os
import argparse

"""This method is created to find all files and directories, given a specific path. Optionally, your can use -name flag
to search only the files that match to a specific name"""


def find(path, name=None):
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
                if os.path.isdir(os.path.join(queue_element, adj)):
                    queue.append(os.path.join(queue_element, adj))

                if not name or (name is not None and adj.startswith(name)):
                    paths_list.append(os.path.join(queue_element, adj))

    paths_list.sort()
    for path in paths_list:
        print path

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('directory')
    parser.add_argument('-name', type=str, default=None)
    args = parser.parse_args()
    find(args.directory, args.name)
