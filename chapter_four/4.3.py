"""Given a sorted (increasing order) array, write an algorithm to create a binary tree with
minimal height."""
class Node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def binary_tree_min_height(self, root, array, final_list):
        if root >= len(array):
            return
        child = self.young_child(root)
        if child + 1 < len(array):
            self.value = array[root]
            self.left = array[child]
            self.right = array[child + 1]
            final_list.insert(root, self)
            self.binary_tree_min_height(child, array, final_list)
            self.binary_tree_min_height(child + 1, array, final_list)

    def young_child(self, parent):
        """this method is created to return the first child, given his parent"""
        return 2 * parent


if __name__ == '__main__':
    array = [0, 3, 5, 7, 9, 12, 15]
    list = [None] * len(array)
    node = Node(None, None, None)
    print node.binary_tree_min_height(1, array, list)
    print list
"""failed"""