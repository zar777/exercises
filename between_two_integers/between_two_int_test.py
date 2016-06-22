import unittest

from two_integers import between_two_int,in_order_visit


class BetweenTwoIntTest(unittest.TestCase):

    def empty_tree_test(self):
        tree = [None, 15, 10, 19, 8, 12, 17, 21]
        array = []
        subtree_dict = {15: [3, 3], 10: [1, 1], 19: [1, 1], 8: [0, 0], 12: [0, 0], 17: [0, 0], 21: [0, 0]}
        in_order_visit(tree, array, 1)