import os
import argparse

"""This method is created to find all files and directories, given a specific path. Optionally, your can use -name flag
to search only the files that match to a specific name"""


def find(path, name=None):
    if not os.path.exists(path):
        return "Path doesn't exist or wrong: please try again"
    stack = []
    stack.append(path)
    while len(stack) > 0:
        stack_element = stack.pop(0)
        if not os.path.islink(stack_element):
            if os.path.isdir(stack_element):
                adj_list = os.listdir(stack_element)
                adj_list.sort(reverse=True)
                for adj in adj_list:
                    stack.insert(0, os.path.join(stack_element, adj))

            last_suffix_stack_el = stack_element.rsplit("/", 1)[1]
            if not name or (name is not None and last_suffix_stack_el.startswith(name)):
                print stack_element
        else:
            print stack_element

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('directory')
    parser.add_argument('-name', type=str, default=None)
    args = parser.parse_args()
    find(args.directory, args.name)
    find("/home/gianluca/Downloads")
    # os.symlink("/home/gianluca/Downloads", "/home/gianluca/Downloads/test/subtest/try")
    # print os.readlink("/home/gianluca/Downloads/test/subtest/try")
    # print str(os.path.islink("/home/gianluca/Downloads/test/subtest/try"))
