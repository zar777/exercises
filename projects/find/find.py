import os
import sys
import argparse


def find(path, name=None, out=sys.stdout):
    """This method is created to find all files and directories, given a specific path.
    Optionally, your can use -name flag to search only the files that match to a specific name"""
    if not os.path.exists(path):
        raise ValueError("Path doesn't exist or wrong: please try again")
    stack = [path]
    while len(stack) > 0:
        element = stack.pop()
        # decided to follow the same implementation of real find in which symlink are not navigate through
        if os.path.isdir(element) and not os.path.islink(element):
            for adj in sorted(os.listdir(element), reverse=True):
                stack.append(os.path.join(element, adj))

        _, filename = os.path.split(element)
        if not name or filename.startswith(name):
            out.write('%s\n' % element)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('directory')
    parser.add_argument('-name', type=str, default=None)
    args = parser.parse_args()
    find(args.directory, args.name)
