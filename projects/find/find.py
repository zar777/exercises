import os
import sys
import argparse

"""This method is created to find all files and directories, given a specific path. Optionally, your can use -name flag
to search only the files that match to a specific name"""


def find(path, name=None, out=sys.stdout):
    if not os.path.exists(path):
        raise ValueError("Path doesn't exist or wrong: please try again")
    stack = [path]
    while len(stack) > 0:
        stack_element = stack.pop(0)
        # decided to follow the same implementation of real find in which symlink are not navigate through
        if os.path.isdir(stack_element) and not os.path.islink(stack_element):
            adj_list = os.listdir(stack_element)
            adj_list.sort()
            for adj in adj_list:
                stack.append(os.path.join(stack_element, adj))

        _, filename = os.path.split(stack_element)
        if not name or filename.startswith(name):
            out.write('%s\n' % stack_element)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('directory')
    parser.add_argument('-name', type=str, default=None)
    args = parser.parse_args()
    find(args.directory, args.name)
