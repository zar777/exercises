import os
import sys
import argparse


def _print_path(path, out):
    if os.path.islink(path):
        out.write('%s' % path + '->' + os.path.realpath(path) + '\n')
    else:
        out.write('%s\n' % path)


def find(path, name=None, out=sys.stdout):
    """This method is created to find all files and directories, given a specific path.
    Optionally, your can use -name flag to search only the files that match to a specific name"""
    if not os.path.exists(path):
        raise ValueError("Path doesn't exist or wrong: please try again")
    marked = set()
    stack = [path]
    while len(stack) > 0:
        curr_path = stack.pop()
        real_path = os.path.realpath(curr_path) if os.path.islink(curr_path) else curr_path
        if real_path not in marked:
            marked.add(curr_path)
            if os.path.isdir(real_path):
                for adj in sorted(os.listdir(real_path), reverse=True):
                    stack.append(os.path.join(real_path, adj))

        # print only if name is not defined or name is in the current path
        if not name or name in curr_path:
            _print_path(curr_path, out)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('directory')
    parser.add_argument('-name', type=str, default=None)
    args = parser.parse_args()
    find(args.directory, args.name)
